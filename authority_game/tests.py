from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):

        if self.round_number == 1:
            yield (views.Introduction, {"q1": int(c(7)), "q2": int(c(9)), "q3": "True", "q4": int(c(6))})
            yield (views.Description)

        if self.player.role() == 'Authority':
            yield (views.Offer, {'offer': int(c(2))})
            yield (views.Decision_Authority, {"decision": 'not perform the Task'})

        if self.player.role() == 'Subordinate':
            yield (views.Decision_Subordinate, {"decision": "not perform the Task"})
            yield (views.Decision_Subordinate_2, {"decision": 'perform the Task'})
            yield (views.Decision_Subordinate_4, {"decision": 'perform the Task'})
        yield (views.Results)

        if self.round_number in [Constants.number_rounds_per_partner * x for x in range(1, Constants.number_partners)]:
            yield (views.ChangeOfPartner)

        if self.round_number == Constants.num_rounds:
            yield (views.Finale_Page)
