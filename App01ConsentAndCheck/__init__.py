import time
import re
import csv

from otree.api import *

c = cu

doc = ''


def read_participants_csv():
    try:

        data = [[], [], [], [], [], [], [],]
        with open(r'./participants.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            _ = next(csv_reader)  # skip header
            for row in csv_reader:
                if row:  # check whether there is a row
                    data[0].append(row[0])
                    data[1].append(row[1])
                    data[2].append(row[2])
                    data[3].append(row[3])
                    data[4].append(row[4])
                    data[5].append(row[5])
                    data[6].append(row[6])

        return data
    except FileNotFoundError:
        return "Error: CSV file not found."
    except Exception as e:
        return f"Error: {str(e)}"


class C(BaseConstants):
    NAME_IN_URL = 'App01ConsentAndCheck'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    VALID_PARTICIPANTS = read_participants_csv()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    CabinID = models.StringField(label='Cabin ID (Format: A01-A20 / B01-B20)')
    PayoutToken = models.StringField(label='Payout Token')
    svo_type = models.StringField(label='svo')
    perfect_stranger_id = models.IntegerField(label='PS ID')

    consent = models.IntegerField(blank=False, choices=[[0, '0'], [1, '1']], label='Consent',
                                  attrs={"invisible": True})
    optInConsent = models.IntegerField(blank=True, initial=0, choices=[[0, '0'], [1, '1']], label='Opt-In Consent',
                                       attrs={"invisible": True})
    colorVideo = models.IntegerField(blank=False, label="What color was mentioned in the video?",
                                     choices=[[0, 'Red'], [1, 'Blue'], [2, 'Green'], [3, 'Yellow']])
    numberVideo = models.IntegerField(blank=False, label="Which number was shown in the video?",
                                      choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])


def CabinID_error_message(player: Player, value):
    cabin_id_validator = re.compile(r'^[A-B](0[1-9]|1[0-9]|20)$')
    if not cabin_id_validator.match(value):
        return "Cabin ID must be in the format A01 to A20 or B01 to B20"


def PayoutToken_error_message(player: Player, value):
    """ Check whether the ID the Participant has entered is in the validation Data"""
    for token, svo_type in zip(C.VALID_PARTICIPANTS[0], C.VALID_PARTICIPANTS[1]):
        if token == value:
            player.participant.svo = svo_type
            print(token)
            return

    return f"Error: Value '{value}' not found in the list for player {player.id_in_group}."


def assign_perfect_stranger_id(group):
    svo1 = [1, 2, 5, 8]
    svo2 = [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    try:
        for p in group.get_players():

            if p.svo_type == 'social':
                temp_id = svo1.pop()
                p.perfect_stranger_id = temp_id
                p.participant.perfect_stranger_id = temp_id
            elif p.svo_type == 'self':
                temp_id = svo2.pop()
                p.perfect_stranger_id = temp_id
                p.participant.perfect_stranger_id = temp_id
            else:
                p.perfect_stranger_id = None
                p.participant.perfect_stranger_id = None
    except IndexError:
        print('There are to much players with svo1 or svo2')


class EnterKD2LabId_byPass(Page):
    """
    This dummy-page is for testing reasons and bypasses...
      - EnterKD2LabId
      - CabinID_error_message
      - PayoutToken_error_message

    Make sure to use in the experiment the EnterKD2LabID Page instead.
    """

    @staticmethod
    def before_next_page(player, timeout_happened):
        # TODO: Add pvq_1, pvq_2, pvq_3, pvq_4, pvq_5 as particiapnt variable (needed in treatment personal values)
        for token, svo_type in zip(C.VALID_PARTICIPANTS[0], C.VALID_PARTICIPANTS[1]):
            if token == f'p{player.id_in_group}':
                player.participant.svo = svo_type

        player.PayoutToken = f'p{int(player.id_in_group)}'

        if player.id_in_group < 10:
            player.CabinID = f'A0{int(player.id_in_group)}'
        if player.id_in_group >= 10:
            player.CabinID = f'A{int(player.id_in_group)}'

        player.svo_type = player.participant.svo


class ConsentFormB_byPass(Page):
    """
    This dummy-page is for testing reasons and bypasses the consent.
    Make sure to use in the experiment the ConsentFormB Page instead.
    """
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.consent = 1
        player.participant.consent = 1
        player.optInConsent = 1
        player.participant.optInConsent = 1


class AudioVideoCheck_byPass(Page):
    """
        This dummy-page is for testing reasons and bypasses the audio and video check.
        Make sure to use in the experiment the AudioVideoCheck Page instead.
    """
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.colorVideo = 2
        player.participant.colorVideo = 2
        player.numberVideo = 3
        player.participant.numberVideo = 3
        player.participant.wait_page_arrival = time.time()  # + random.randint(0, 200)


class WaitForAll(WaitPage):
    """
    This page waits for all players to arrive to ca call assign_perfect_stranger_id function,
    which handles the id's based on the svo and control for the right self:social-ratio
    """
    after_all_players_arrive = assign_perfect_stranger_id

page_sequence = [
    EnterKD2LabId_byPass,
    ConsentFormB_byPass,
    AudioVideoCheck_byPass,
    WaitForAll
]