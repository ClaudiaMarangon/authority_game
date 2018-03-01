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
    name_in_url = 'final_payoff'
    players_per_group = None
    num_rounds = 1
    currency_change = 0.025



class Subsession(BaseSubsession):
    def creating_session(self):
        n_player = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        for p in self.get_players():
            p.lucky = random.choice(n_player)
            n_player.remove(p.lucky)

    pass


class Group(BaseGroup):

    def set_val(self):
        for p in self.get_players():
            p.payoff_practice = p.participant.vars['pay']
           # p.payoff_simple_task = p.participant.vars['pay_nooffer']
            p.payoff_task = p.participant.vars['task_payoff']
            p.payoff_money = p.participant.vars['money_pay']
            p.payoff_circle = p.participant.vars['circlet_payoff']
    pass


class Player(BasePlayer):
    payoff_practice = models.FloatField()
    #payoff_simple_task = models.FloatField()
    payoff_task = models.FloatField()
    payoff_money = models.FloatField()
    payoff_circle = models.FloatField()
    payoff_final = models.FloatField()
    lucky = models.IntegerField()

    def set_payoff(self):
        if self.lucky != 13:
            self.participant.payoff = self.participant.payoff - self.participant.vars['pay']
            self.payoff_final = self.participant.vars['task_payoff'] + self.participant.vars['money_pay'] + self.participant.vars['circlet_payoff']
        else:
            self.payoff_final = self.participant.vars['task_payoff'] + self.participant.vars['money_pay'] + self.participant.vars['circlet_payoff'] + self.participant.vars['pay']



    pass
