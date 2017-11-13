from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):

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

        if self.round_number in [8, 16, 24, 32]:
            yield (views.ChangeOfPartner)

        if self.round_number == 40:
            yield (views.Finale_Page)