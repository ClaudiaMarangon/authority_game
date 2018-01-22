from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return {
            'role': self.player.role(),
            'other_role': self.player.other_role()
        }
    pass

class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']
    def vars_for_template(self):
        return {
            'round': self.round_number,
            'role': self.player.role(),
            'other_role': self.player.other_role()
        }
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()
        pass


class Results(Page):
    def vars_for_template(self):
        return {
            'other_dec': self.player.other_player().decision,
            'other_pay': self.player.other_player().payoff,
        }
    pass

class ChangeRole(Page):
    def is_displayed(self):
        return self.round_number==21

    def vars_for_template(self):
        return {
            'role': self.player.role()
        }
    pass
page_sequence = [
    ChangeRole,
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
