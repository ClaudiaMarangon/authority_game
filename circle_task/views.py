from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




class Choice(Page):
    form_model = models.Player
    form_fields = ['choice', 'otherpay']
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoffs()
    pass

class Results(Page):
    pass


page_sequence = [
    Choice,
    ResultsWaitPage,
    Results,
]
