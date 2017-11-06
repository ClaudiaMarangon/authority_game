from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'circle_task'
    players_per_group = 2
    num_rounds = 1
    endowment = float(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    choicep1 = models.FloatField()
    def set_payoff(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = float(self.choicep1)
        p2.payoff = Constants.endowment - float(self.choicep1)
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'P1'
        else:
            return 'P2'

    pass
