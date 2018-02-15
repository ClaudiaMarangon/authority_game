from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'authority_game_noffer'
    players_per_group = 2
    num_rounds = 40
    authority_c = c(5)
    authority_rr = c(3)
    exploit_payoff = c(10)
    subordinate_rr = c(5)
    subordinate_c = c(7)


class Subsession(BaseSubsession):

    pass


class Group(BaseGroup):

    def set_payoff(self):

        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['pay_nooffer'] = 0

            if p.role()=='Authority':
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
                p.payoff = payoff_matrix[p.decision][p.other_player().decision]
                p.participant.vars['pay_nooffer'] = p.participant.vars['pay_nooffer'] + p.payoff
            else:
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
                p.payoff = payoff_matrix[p.decision][p.other_player().decision]
                p.participant.vars['pay_nooffer'] = p.participant.vars['pay_nooffer'] + p.payoff

    pass


class Player(BasePlayer):

    decision = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        widget=widgets.RadioSelect
    )

    def role(self):
        if self.round_number<=20:
            if self.id_in_group == 1:
                return 'Authority'
            else:
                return 'Subordinate'
        else:
            if self.id_in_group == 2:
                return 'Authority'
            else:
                return 'Subordinate'

    def other_role(self):
        if self.round_number <= 20:
            if self.id_in_group == 2:
                return 'Authority'
            else:
                return 'Subordinate'
        else:
            if self.id_in_group == 1:
                return 'Authority'
            else:
                return 'Subordinate'

    def other_player(self):
        return self.get_others_in_group()[0]
    pass
