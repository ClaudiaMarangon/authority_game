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
    num_rounds = 2
    authority_c = c(5)
    authority_rr = c(3)
    exploit_payoff = c(10)
    subordinate_rr = c(5)
    subordinate_c = c(7)
    computer_choices = ['perform the Task', 'not perform the Task']

class Subsession(BaseSubsession):

    def creating_session(self):
        for g in self.get_groups():
            if self.round_number <20:
                g.get_player_by_id(1).role = 'authority'
                g.get_player_by_id(2).role = 'subordinate'
            else:
                g.get_player_by_id(2).role = 'authority'
                g.get_player_by_id(1).role = 'subordinate'

        for p in self.get_players():
            p.computer_choice = random.choice(Constants.computer_choices)

    pass


class Group(BaseGroup):

    def set_payoffs(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['pay'] = 0
                p.participant.vars['cpay'] = 0
            if p.role == 'authority':
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
                p.payoff = payoff_matrix[p.mychoice][p.computer_choice]
                p.participant.vars['pay'] = p.participant.vars['pay'] + p.payoff
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
                p.payoff_c = payoff_matrix_c[p.computer_choice][p.mychoice]
                p.participant.vars['cpay'] = p.participant.vars['cpay'] + p.payoff_c

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
            p.payoff_c = payoff_matrix_c[p.computer_choice][p.mychoice]
            p.participant.vars['cpay'] = p.participant.vars['cpay'] + p.payoff_c

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
            p.payoff = payoff_matrix[p.mychoice][p.computer_choice]
            p.participant.vars['pay'] = p.participant.vars['pay'] + p.payoff

    pass


class Player(BasePlayer):
    role = models.CharField()
    payoff_c = models.IntegerField()
    computer_choice = models.CharField(
        choices=['perform the Task', 'not perform the Task']
    )

    mychoice = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        widget=widgets.RadioSelect
    )

    pass
