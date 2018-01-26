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

    def creating_session(self):
        for p in self.get_players():
            p.payoff_practice = p.participant.vars['pay']
            p.payoff_simple_task = p.participant.vars['pay_nooffer']
            p.payoff_task = p.participant.vars['task_payoff']
            p.payoff_money = p.participant.vars['money_pay']
            p.payoff_circle = p.participant.vars['circlet_payoff']
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    payoff_practice = models.FloatField()
    payoff_simple_task = models.FloatField()
    payoff_task = models.FloatField()
    payoff_money = models.FloatField()
    payoff_circle = models.FloatField()

    def set_payoff(self):
        self.payoff = self.payoff_simple_task + self.payoff_task + self.payoff_money + self.payoff_circle
        self.participant.vars['final_payoff'] = self.payoff
    pass
