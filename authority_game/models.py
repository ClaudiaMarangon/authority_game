from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Claudia Marangon & Caroline Lebrun'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'authority_game'
    players_per_group = 2
    number_partners = 60
    number_rounds_per_partner = 1
    num_rounds = number_partners * number_rounds_per_partner
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
    def creating_session(self):
        if self.round_number in [1 + Constants.number_rounds_per_partner * x for x in range(Constants.number_partners)]:
            self.group_randomly(fixed_id_in_group=True)
        else:
            self.group_like_round(self.round_number - 1)


class Group(BaseGroup):

    offer = models.CurrencyField(
        initial=0,
        choices=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5],
        widget=widgets.RadioSelect
    )
    decision_auth = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        widget=widgets.RadioSelect,
    )

    decision_sub0 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 0 tokens you would:',
        widget=widgets.RadioSelect
    )

    decision_sub0_5 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 0.5 tokens you would:',
        widget=widgets.RadioSelect
    )

    decision_sub1 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 1 token you would:',
        widget=widgets.RadioSelect
    )

    decision_sub1_5 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 1.5 tokens you would:',
        widget=widgets.RadioSelect
    )

    decision_sub2 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 2 tokens you would:',
        widget=widgets.RadioSelect
    )

    decision_sub2_5 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 2.5 tokens you would:',
        widget=widgets.RadioSelect
    )

    decision_sub3 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 3 tokens you would:',
        widget=widgets.RadioSelect
    )

    decision_sub3_5 = models.CharField(
        choices=['perform the Task', 'not perform the Task'],
        verbose_name='If the Authority offered you 3.5 tokens you would:',
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

        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['task_payoff'] = 0

            if self.offer == 0:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub0]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub0][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 0.5:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub0_5]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub0_5][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 1:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub1]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub1][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 1.5:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub1_5]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub1_5][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 2:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub2]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub2][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 2.5:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub2_5]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub2_5][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 3:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub3_5]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub3_5][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

            if self.offer == 3.5:
                if p.role() == 'Authority':
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.authority_cc(),
                                'not perform the Task': Constants.authority_cr
                            },
                        'not perform the Task':
                            {
                                'perform the Task': self.authority_rc(),
                                'not perform the Task': Constants.authority_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_auth][self.decision_sub3_5]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff
                else:
                    payoff_matrix = {
                        'perform the Task':
                            {
                                'perform the Task': self.subordinate_cc(),
                                'not perform the Task': self.subordinate_rc()
                            },
                        'not perform the Task':
                            {
                                'perform the Task': Constants.exploit_payoff,
                                'not perform the Task': Constants.subordinate_rr
                            }
                    }
                    p.payoff = payoff_matrix[self.decision_sub3_5][self.decision_auth]
                    p.participant.vars['task_payoff'] = p.participant.vars['task_payoff'] + p.payoff

    pass


class Player(BasePlayer):

    offer_try = models.FloatField(
        choices = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5],
        widget = widgets.RadioSelect
    )

    def role(self):
        if self.round_number<=30:
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
        if self.round_number <= 30:
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
