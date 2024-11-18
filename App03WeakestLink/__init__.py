from otree.api import *
import random

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'App03WeakestLink'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    ENDOWMENT = 200


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class VVC(Page):
    form_model = 'player'
    timeout_seconds = 600

    @staticmethod
    def vars_for_template(player: Player):
        optInConsent = player.participant.optInConsent
        return dict(optInConsent=optInConsent)

    # TODO: Please use this page to implement the treatments


page_sequence = [
    VVC,
]
