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
    name_in_url = 'practice_game_control'
    players_per_group = 2
    num_rounds = 40
    authority_c = c(5)
    authority_rr = c(3)
    exploit_payoff = c(10)
    subordinate_rr = c(5)
    subordinate_c = c(7)
    computer_choices_s = ['perform the Task', 'perform the Task', 'perform the Task', 'perform the Task',
                          'not perform the Task']
    computer_choices_a = ['perform the Task', 'not perform the Task', 'not perform the Task', 'not perform the Task',
                          'not perform the Task']


class Subsession(BaseSubsession):

    def creating_session(self):
        for g in self.get_groups():
            if self.round_number <=20:
                g.get_player_by_id(1).role = 'authority'
                g.get_player_by_id(2).role = 'subordinate'
            else:
                g.get_player_by_id(2).role = 'authority'
                g.get_player_by_id(1).role = 'subordinate'

        for p in self.get_players():
            if p.role == 'subordinate':
                p.computer_choice = random.choice(Constants.computer_choices_a)
            else:
                p.computer_choice = random.choice(Constants.computer_choices_s)

    pass


class Group(BaseGroup):


    pass


class Player(BasePlayer):

    name = models.CharField(
        verbose_name="Please enter your First Name:"
    )

    surname = models.CharField(
        verbose_name="Please enter your Last Name:"
    )

    mail = models.CharField(
        verbose_name="Please enter the email adress where you want to receive the payment"
    )

    role = models.CharField()
    payoff_c = models.IntegerField()
    computer_choice = models.CharField(
        choices=['perform the Task', 'not perform the Task']
    )

    mychoice = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        widget=widgets.RadioSelect
    )

    def set_payoffs(self):
        if self.round_number == 1:
            self.participant.vars['pay'] = 0
            self.participant.vars['cpay'] = 0


        if self.role == 'authority':
            payoff_matrix = {
                'perform the Task':
                    {
                        'perform the Task': Constants.authority_c,
                        'not perform the Task': Constants.authority_c
                    },
                'not perform the Task':
                    {
                        'perform the Task': Constants.exploit_payoff,
                        'not perform the Task': Constants.authority_rr
                    }
            }
            self.payoff = payoff_matrix[self.mychoice][self.computer_choice]
            self.participant.vars['pay'] = self.participant.vars['pay'] + self.payoff
            payoff_matrix_c = {
                'perform the Task':
                    {
                        'perform the Task': Constants.subordinate_c,
                        'not perform the Task': Constants.subordinate_c
                    },
                'not perform the Task':
                    {
                        'perform the Task': Constants.exploit_payoff,
                        'not perform the Task': Constants.subordinate_rr
                    }
            }
            self.payoff_c = payoff_matrix_c[self.computer_choice][self.mychoice]
            self.participant.vars['cpay'] = self.participant.vars['cpay'] + self.payoff_c

        else:
            payoff_matrix_c = {
                'perform the Task':
                    {
                        'perform the Task': Constants.authority_c,
                        'not perform the Task': Constants.authority_c
                    },
                'not perform the Task':
                    {
                        'perform the Task': Constants.exploit_payoff,
                        'not perform the Task': Constants.authority_rr
                    }
            }
            self.payoff_c = payoff_matrix_c[self.computer_choice][self.mychoice]
            self.participant.vars['cpay'] = self.participant.vars['cpay'] + self.payoff_c

            payoff_matrix = {
                'perform the Task':
                    {
                        'perform the Task': Constants.subordinate_c,
                        'not perform the Task': Constants.subordinate_c
                    },
                'not perform the Task':
                    {
                        'perform the Task': Constants.exploit_payoff,
                        'not perform the Task': Constants.subordinate_rr
                    }
            }
            self.payoff = payoff_matrix[self.mychoice][self.computer_choice]
            self.participant.vars['pay'] = self.participant.vars['pay'] + self.payoff

    pass
