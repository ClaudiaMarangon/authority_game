from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

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

    def vars_for_template(self):
        return {
            'round': self.round_number,
            'role': self.player.role(),
            'other_role': self.player.other_role()
        }
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
    form_fields = ['decision_sub0', 'decision_sub0_5','decision_sub1','decision_sub1_5','decision_sub2','decision_sub2_5', 'decision_sub3', 'decision_sub3_5']

    def vars_for_template(self):
        return {
            'round': self.round_number,
            'role': self.player.role(),
            'other_role': self.player.other_role()
        }

    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
    pass

class Results(Page):


    def vars_for_template(self):

        if self.player.role() == 'Authority':
            if self.group.offer == 0:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub0,
                    'same_choice': self.group.decision_auth == self.group.decision_sub0,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 0.5:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub0_5,
                    'same_choice': self.group.decision_auth == self.group.decision_sub0_5,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 1:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub1,
                    'same_choice': self.group.decision_auth == self.group.decision_sub1,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 1.5:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub1_5,
                    'same_choice': self.group.decision_auth == self.group.decision_sub1_5,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 2:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub2,
                    'same_choice': self.group.decision_auth == self.group.decision_sub2,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 2.5:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub2_5,
                    'same_choice': self.group.decision_auth == self.group.decision_sub2_5,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 3:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub3,
                    'same_choice': self.group.decision_auth == self.group.decision_sub3,
                }

        if self.player.role() == 'Authority':
            if self.group.offer == 3.5:
                return {
                    'my_decision': self.group.decision_auth,
                    'other_player_decision': self.group.decision_sub3_5,
                    'same_choice': self.group.decision_auth == self.group.decision_sub3_5,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 0:
                return {
                    'my_decision': self.group.decision_sub0,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub0,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 0.5:
                return {
                    'my_decision': self.group.decision_sub0_5,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub0_5,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 1:
                return {
                    'my_decision': self.group.decision_sub1,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub1,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 1.5:
                return {
                    'my_decision': self.group.decision_sub1_5,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub1_5,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 2:
                return {
                    'my_decision': self.group.decision_sub2,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub2,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 2.5:
                return {
                    'my_decision': self.group.decision_sub2_5,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub2_5,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 3:
                return {
                    'my_decision': self.group.decision_sub3,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub3,
                }

        if self.player.role() == 'Subordinate':
            if self.group.offer == 3.5:
                return {
                    'my_decision': self.group.decision_sub3_5,
                    'other_player_decision': self.group.decision_auth,
                    'same_choice': self.group.decision_auth == self.group.decision_sub3_5,
                }


class ChangeOfPartner(Page):
    def is_displayed(self):
        return self.round_number in [Constants.number_rounds_per_partner * x for x in
                                     range(1, Constants.number_partners)]


class Finale_Page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class ChangeRole(Page):
    def is_displayed(self):
        return self.round_number==41

    def vars_for_template(self):
        return {
            'role': self.player.role()
        }
    pass

page_sequence = [
    ChangeRole,
    Introduction,
    Offer,
    Decision_Authority,
    Decision_Subordinate,
    ResultsWaitPage,
    Results,
    ChangeOfPartner,
    Finale_Page
]
