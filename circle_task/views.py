from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




class ChoiceP1(Page):
    form_model = models.Group
    form_fields = ['choicep1']
    def is_displayed(self):
        return self.player.role() == 'P1'
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
        return
    pass

class Results(Page):
    def vars_for_template(self):
        return {
            'player1' : self.player.role == 'P1',
            'player2': self.player.role == 'P2',
        }
    pass


page_sequence = [
    ChoiceP1,
    ResultsWaitPage,
    Results,
]
