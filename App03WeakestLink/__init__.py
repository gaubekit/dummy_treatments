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

            }



page_sequence = [
    MentalContrasting
]