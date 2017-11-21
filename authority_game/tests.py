from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):

        if self.round_number == 1:
            yield (views.Introduction, {"q1": c(7), "q2": c(9), "q3": "True", "q4": c(6)})
            yield (views.Description)

        if self.player.role() == 'Authority':
            yield (views.Offer, {'offer': c(2)})
            yield (views.Decision_Authority, {"decision": 'Refuse'})

        if self.player.role() == 'Subordinate':
            yield (views.Decision_Subordinate, {"decision": "Refuse"})
            yield (views.Decision_Subordinate_2, {"decision": 'Contribute'})
            yield (views.Decision_Subordinate_4, {"decision": 'Contribute'})
        yield (views.Results)

        if self.round_number in [Constants.number_rounds_per_partner * x for x in range(1, Constants.number_partners)]:
            yield (views.ChangeOfPartner)

        if self.round_number == Constants.num_rounds:
            yield (views.Finale_Page)
