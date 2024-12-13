from otree.api import *
import random

from otree.models import group

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'XXTestnameXX' # Platzhalter
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    ENDOWMENT = 200



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
     notes_outcome = models.StringField(blank = True)
     notes_name = models.StringField(blank = True)
     notes_obstacle = models.StringField(blank = True)
     timeout_seconds = models.IntegerField(initial=480)
     pass




class MentalContrasting(Page):
    template_name = 'treatment_page/Template_Video_Meeting_AKTUELL.html'
    timeout_seconds = 480  # Gesamtzeit: 8:00 Minuten
    group_by_arrival_time = True  # Spieler in Gruppen von 4

    def vars_for_template(self):
            return {
                'group_id': self.group.id_in_subsession,
                'timeout_seconds': self.timeout_seconds,
                'texts':{
                    'outcome_notes':
                        "Your goal is to spend an enjoyable vacation.<br>" +
                        "<br>" +
                        "What would be the best outcome for you? <br>" +
                        "<br>" +
                        "Think about it and write down a short note <b><u>individually</u></b>.",

                    'outcome_imagination':
                        "<b><u>Individually</u></b> imagine the outcome as vividly and clearly as possible.<br>" +
                        "<br>" +
                        "Feel free to close your eyes.",

                    'outcome_meeting':
                        "Please share your thoughts about the outcome with <b><u>your team</u></b>.",

                    'obstacle_notes':
                        "What obstacles might the team face?<br>" +
                        "<br>" +
                        "Think about it and write down a short note <b><u>individually</u></b>.",

                    'obstacle_imagination':
                        "<b><u>Individually</u></b> imagine the obstacle you find hardest to overcome.<br>" +
                        "<br>" +
                        "Feel free to close your eyes.",

                    'obstacle_meeting':
                        "Please share your thoughts about the most challenging obstacles with <b><u>your team</u></b>.",

                    'rules_notes':
                        "What collaboration rules could help your team overcome obstacles?<br>" +
                        "<br>" +
                        "Think about it and write down a short note <b><u>individually</u></b>.",

                    'rules_imagination':
                        "<b><u>Individually</u></b> imagine how the holiday would be with this rules.<br>" +
                        "<br>" +
                        "Feel free to close your eyes.",

                    'rules_meeting':
                        "Please share and discuss your collaboration rules with <b><u>your team</u></b>.",

                    'announcement':
                        "Announcement in progress..."


            }
                }





page_sequence = [
    MentalContrasting
]