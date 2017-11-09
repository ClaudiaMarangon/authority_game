from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Introduction(Page):
    form_model = models.Player
    form_fields = ['question1', 'question2', 'question3', 'question4']
    pass

class Offer(Page):

    def is_displayed(self):
        return self.player.role() == 'Authority'
    form_model = models.Group
    form_fields = ['offer']
    pass


class Decision_Authority(Page):

    def is_displayed(self):
        return self.player.role() == 'Authority'
    form_model = models.Player
    form_fields = ['decision']
    pass


class Decision_Subordinate(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Player
    form_fields = ['decision']
    pass


class Decision_Subordinate_2(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Player
    form_fields = ['decision']
    pass


class Decision_Subordinate_4(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Player
    form_fields = ['decision']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass

class Results(Page):

    def vars_for_template(self):
        return {
            'my_decision': self.player.decision,
            'other_player_decision': self.player.other_player().decision,
            'same_choice': self.player.decision == self.player.other_player().decision,
        }



page_sequence = [
    Introduction,
    Offer,
    Decision_Authority,
    Decision_Subordinate,
    Decision_Subordinate_2,
    Decision_Subordinate_4,
    ResultsWaitPage,
    Results,
]
