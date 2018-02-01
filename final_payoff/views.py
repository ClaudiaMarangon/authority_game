from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    def before_next_page(self):
        return {self.player.set_payoff(),  self.group.set_val()}

    pass

class Results(Page):
    def vars_for_template(self):
        return {
            'euro_pay': self.player.real_world_c()
        }
    pass


page_sequence = [
    MyPage,
    Results
]
