from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math

author = 'Claudia Marangon'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'circle_task'
    players_per_group = 2
    num_rounds = 1
    endowmentsqr = float(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.FloatField()
    otherpay = models.FloatField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def partner_choice(self):
        return self.other_player().choice

    def partner_yourp(self):
        return self.other_player().otherpay

    def set_payoffs(self):
        self.payoff = self.choice + self.partner_yourp()
        self.participant.vars['circlet_payoff'] = self.payoff
    pass
