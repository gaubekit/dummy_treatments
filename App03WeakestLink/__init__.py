from otree.api import *
import random

from otree.models import group

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
    notes_outcome = models.StringField(blank = True)
    notes_name = models.StringField(blank = True)
    notes_obstacle = models.StringField(blank = True)
    pass


class VVC(Page):
    form_model = 'player'
    timeout_seconds = 600

    @staticmethod
    def vars_for_template(player: Player):
        optInConsent = player.participant.optInConsent
        return dict(optInConsent=optInConsent)

    # TODO: Please use this page to implement the treatments

class BlueprintPage(Page):
    template_name = 'treatment_page/treatment_blueprint.html'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'variable_template': 'v1.0',
        }

class TreatmentInteraction(Page):
    def vars_for_template(self):
        spider_values = [4, 3, 5, 2, 4] 
        return {
            "spider_values": spider_values,
        }



#Page to get name of players to use later
class PlayerName(Page):
    template_name = 'treatment_page/treatment_note_blueprint.html'
    # connect HTML input with data from player
    form_model = 'player'
    form_fields = ['notes_name']
    timeout_seconds = 20

    @staticmethod
    def vars_for_template(self):
        return {
            'title' : 'Please type in your name!',
            'description' : 'Please press save, otherwise your input will be lost.',

        }
    @staticmethod
    def error_message(player, values):
        if not values['notes_name']:
            return 'Zone can not be empty!'


#Page to explain the next step
class BlueprintExplanation1(Page):
    template_name = 'treatment_page/treatment_explanation_blueprint.html'
    # connect HTML input with data from player
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'title': 'Step 1',
            'description': 'When functioning as a team results in experiencing an enjoyable holiday: What would be the best outcome for you personally? On the next page you will have 30 seconds to think about this individually and jot down a short note.'
        }


#Page for taking notes on the best outcome
class BlueprintNote1(Page):
    template_name = 'treatment_page/treatment_note2_blueprint.html'
    # connect HTML input with data from player
    form_model ='player'
    form_fields = ['notes_outcome']
    timeout_seconds = 30

    @staticmethod
    def vars_for_template(self):
        return {'title': 'Take notes:',
                'description': 'What would be the best outcome for you personally for the holiday setting? Please press save, otherwise your answer will get lost.',}


    @staticmethod
    def error_message(player, values):
        if not values['notes_outcome']:
            return 'Zone can not be empty!'



#Page for imagining the best outcome
class BlueprintImagination1(Page):
    template_name ='treatment_page/treatment_imagination_blueprint.html'
    timeout_seconds = 45

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'title': 'Step 2',
            'description': 'Please take the next 45 seconds to close your eyes and imagine that outcome as vividly as possible in your thoughts. Feel free to close your eyes - a sound will bring you back!'

        }
#Page to explain them the next step that players can use the next 90 seconds as efficient as possible
class BlueprintExplanation2(Page):
    template_name = 'treatment_page/treatment_explanation_blueprint.html'
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'title': 'Your next task will be:',
            'description' : 'In the next step you will have 90 seconds to discuss with your team about an outcome that is acceptable for all members.'
        }
#Page to start the video meeting and show the notes of all members
class Videomeeting1(Page):
    template_name = 'treatment_page/treatment_discussion_alternative_blueprint.html'
    timeout_seconds = 90

    @staticmethod
    def vars_for_template(self):

            notes = []
            for p in self.group.get_players():
                notes.append({
                    'player_name': p.notes_name if p.notes_name else 'No name',
                    'text': p.notes_outcome if p.notes_outcome else 'No notes'
                })

            return {
                'notes': notes,
                'instructions_text': "Welcome! Please use your camera and microphone!.",
            }


class BlueprintExplanation3(Page):
    template_name = 'treatment_page/treatment_explanation_blueprint.html'
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'title': 'Your next task will be:',
            'description' : 'In the next step you will have 30 Seconds time to think about individually, what is hindering you as a team from having this enjoyable holiday. Please take notes in this next step! '
        }


class BlueprintNote2(Page):
    template_name = 'treatment_page/treatment_note3_blueprint.html'
    form_model = 'player'
    form_fields = ['notes_obstacle']
    timeout_seconds = 30

    @staticmethod
    def vars_for_template(self):
        return{
            'title': 'Take notes',
            'description': 'What is hindering you as a team from having an enjoyable vacation? Please press submit, otherwise your information will get lost.',

        }

    @staticmethod
    def error_message(player, values):
        if not values['notes_obstacle']:
            return 'Zone can not be empty!'


class BlueprintImagination2(Page):
    template_name = 'treatment_page/treatment_imagination_blueprint.html'
    timeout_seconds = 45

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'title': 'Take a moment to imagine:',
            'description' : 'What is the obstacle, that is personally the hardest for you to overcome. You may close your eyes - a sound will bring you back in 45 seconds'
        }

class BlueprintExplanation4(Page):
    template_name = 'treatment_page/treatment_explanation_blueprint.html'
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'title': 'Your next task will be:',
            'description': 'Use the next 90 seconds to share your thoughts with the team and discover what you have in common. Your notes about the obstacle will again be shared.'
        }

class Videomeeting2(Page):
    template_name = 'treatment_page/treatment_discussion_blueprint.html'
    timeout_seconds = 90

    @staticmethod
    def vars_for_template(self):

            notes = []
            for p in self.group.get_players():
                notes.append({
                    'player_name': p.notes_name if p.notes_name else 'No name',
                    'text': p.notes_obstacle if p.notes_obstacle else 'No notes'
                })

            return {
                'notes': notes,
                'instructions_text': "Welcome! Please use your camera and microphone!.",
            }
class ThankYou(Page):
    template_name = 'treatment_page/treatment_explanation_blueprint.html'

    @staticmethod
    def vars_for_template(self):
        return{
            'title' : 'Thank You!',
            'description' : 'Your participation is highly appreciated!'
        }
page_sequence = [
    VVC,
    PlayerName,#20 seconds
    BlueprintExplanation1,#15 seconds
    BlueprintNote1,#30 seconds
    BlueprintImagination1,#45 seconds
    BlueprintExplanation2,#15 seconds
    Videomeeting1,#90 seconds
    BlueprintExplanation3,#15 seconds
    BlueprintNote2,#30 seconds
    BlueprintImagination2,#45 seconds
    BlueprintExplanation4,#15 seconds
    Videomeeting2,#90 seconds => 410 seconds => 70 seconds free
    ThankYou

]