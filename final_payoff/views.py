from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    def before_next_page(self):
        return {self.player.set_payoff(),  self.group.set_val()}

    pass

class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
