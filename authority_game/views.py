from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Introduction(Page):

    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4']

    def error_message(self, values):
        if not (values["q1"] == Constants.answ1):
            return 'You got question 1 wrong!'

        if not (values["q2"] == Constants.answ2):
            return 'You got question 2 wrong!'

        if not (values["q3"]):
            return 'You got question 3 wrong!'

        if not (values["q4"] == Constants.answ4):
            return 'You got question 4 wrong!'
    pass

class Description(Page):
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

class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        if self.group.offer == 0:
            return {self.player.role() == 'Authority',
                    self.player.role() == 'Subordinate'}
        else:
            return self.player.role() == 'Subordinate'


    def after_all_players_arrive(self):
        if self.group.offer == 0:
            self.group.set_payoff()
        pass

class Decision_Subordinate_2(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Player
    form_fields = ['decision']
    pass

class ResultsWaitPage2(WaitPage):

    def is_displayed(self):
        if self.group.offer == 2:
            return {self.player.role() == 'Authority',
                    self.player.role() == 'Subordinate'}
        else:
            return self.player.role() == 'Subordinate'

    def after_all_players_arrive(self):
        if self.group.offer == 2:
            self.group.set_payoff()
        pass

class Decision_Subordinate_4(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Player
    form_fields = ['decision']
    pass


class ResultsWaitPage4(WaitPage):

    def is_displayed(self):
        if self.group.offer == 4:
            return {self.player.role() == 'Authority',
                    self.player.role() == 'Subordinate'}
        else:
            return self.player.role() == 'Subordinate'

    def after_all_players_arrive(self):
        if self.group.offer == 4:
            self.group.set_payoff()
        pass

class Results(Page):

    def vars_for_template(self):
        return {
            'my_decision': self.player.decision,
            'other_player_decision': self.player.other_player().decision,
            'same_choice': self.player.decision == self.player.other_player().decision,
        }


class ChangeOfPartner(Page):
    def is_displayed(self):
        return self.round_number in [8, 16, 24, 32]

class Finale_Page(Page):
    def is_displayed(self):
        return self.round_number == 40



page_sequence = [
    Introduction,
    Description,
    Offer,
    Decision_Authority,
    Decision_Subordinate,
    ResultsWaitPage,
    Decision_Subordinate_2,
    ResultsWaitPage2,
    Decision_Subordinate_4,
    ResultsWaitPage4,
    Results,
    ChangeOfPartner,
    Finale_Page
]
