from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'authority_game'
    players_per_group = 2
    num_rounds = 1
    authority_cr = c(5)
    authority_rr = c(3)
    exploit_payoff = c(10)
    subordinate_rr = c(5)
    subordinate_c = c(7)
    answ1 = c(7)
    answ2 = c(9)
    answ4 = c(6)
    pass

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    offer = models.CurrencyField(
        initial=0,
        choices=[0, 2, 4],
        widget=widgets.RadioSelect
    )

    def authority_rc(self):
        return Constants.exploit_payoff - self.offer

    def subordinate_cc(self):
        return Constants.subordinate_c + self.offer

    def subordinate_rc(self):
        return Constants.subordinate_c + self.offer

    def authority_cc(self):
        return Constants.authority_cr - self.offer

    def set_payoff(self):
        authority = self.get_player_by_id(1)
        subordinate = self.get_player_by_id(2)

        authority.payoff_matrix = {
            'Contribute':
                {
                    'Contribute': self.authority_cc(),
                    'Refuse': Constants.authority_cr
                },
            'Refuse':
                {
                    'Contribute': self.authority_rc(),
                    'Refuse': Constants.authority_rr
                }
        }
        authority.payoff = authority.payoff_matrix[authority.decision][authority.other_player().decision]

        subordinate.payoff_matrix = {
            'Contribute':
                {
                    'Contribute': self.subordinate_cc(),
                    'Refuse': self.subordinate_rc()
                },
            'Refuse':
                {
                    'Contribute': Constants.exploit_payoff,
                    'Refuse': Constants.subordinate_rr
                }
            }
        subordinate.payoff = subordinate.payoff_matrix[subordinate.decision][subordinate.other_player().decision]
    pass


class Player(BasePlayer):

    q1 = models.PositiveIntegerField(
        verbose_name="Please, enter your answer below"
    )
    q2 = models.PositiveIntegerField(
        verbose_name="Please, enter your answer below"
    )
    q3 = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[
            [True, 'True'],
            [False, 'False'],
        ],
        verbose_name="True or False?"
    )
    q4 = models.PositiveIntegerField(
        verbose_name="Please, enter your answer below"
    )

    decision = models.CharField(
        choices=['Contribute', 'Refuse'],
        widget=widgets.RadioSelect
    )

    def role(self):
        if self.id_in_group == 1:
            return 'Authority'
        if self.id_in_group == 2:
            return 'Subordinate'

    def other_role(self):
        if self.id_in_group == 1:
            return 'Subordinate'
        if self.id_in_group == 2:
            return 'Authority'

    def other_player(self):
        return self.get_others_in_group()[0]

    pass
