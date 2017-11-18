from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'final_payoff'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        self.ct_payoff = self.participant.vars['circlet_payoff']
        self.tg_payoff = self.participant.vars['task_payoff']
        self.payoff = self.ct_payoff + self.tg_payoff
        self.participant.vars['final_payoff'] = self.payoff
    pass
