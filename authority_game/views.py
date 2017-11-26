from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

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
    def is_displayed(self):
        return self.round_number == 1
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
    form_model = models.Group
    form_fields = ['decision_auth']
    pass


class Decision_Subordinate(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Group
    form_fields = ['decision_sub0']
    pass


class Decision_Subordinate_2(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Group
    form_fields = ['decision_sub2']
    pass


class Decision_Subordinate_4(Page):

    def is_displayed(self):
        return self.player.role() == 'Subordinate'
    form_model = models.Group
    form_fields = ['decision_sub4']
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()

    pass

class Results(Page):

    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['task_payoff'] = self.player.payoff
        else:
            self.player.participant.vars['task_payoff'] = self.player.participant.vars['task_payoff'] + self.player.payoff


    def vars_for_template(self):

        if self.player.role() == 'Authority':
            if self.group.offer == 0:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub0,
                    'same_choice': self.group.decision_auth == self.group.decision_sub0,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 2:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub2,
                    'same_choice': self.group.decision_auth == self.group.decision_sub2,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 4:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub4,
                    'same_choice': self.group.decision_auth == self.group.decision_sub4,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 0:
                return {
                    'my_decision': self.group.decision_sub0,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub0,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 2:
                return {
                    'my_decision': self.group.decision_sub2,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub2,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 4:
                return {
                    'my_decision': self.group.decision_sub4,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub4,
                }


class ChangeOfPartner(Page):
    def is_displayed(self):
        return self.round_number in [Constants.number_rounds_per_partner * x for x in
                                     range(1, Constants.number_partners)]


class Finale_Page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds




page_sequence = [
    Introduction,
    Description,
    Offer,
    Decision_Authority,
    Decision_Subordinate,
    Decision_Subordinate_2,
    Decision_Subordinate_4,
    ResultsWaitPage,
    Results,
    ChangeOfPartner,
    Finale_Page
]
