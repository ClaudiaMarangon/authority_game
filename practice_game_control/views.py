from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Payement_Info(Page):
    def is_displayed(self):
        return self.round_number==1

    form_model = models.Player
    form_fields = ['name', 'surname', 'mail']
    pass

class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1

    pass


class VSComputer(Page):
    def is_displayed(self):
        return self.round_number == 1

    pass

class Authority(Page):
    def is_displayed(self):
        return self.player.role == 'authority'

    form_model = models.Player
    form_fields = ['mychoice']
    def vars_for_template(self):
        return {
            'round': self.round_number,
            'authority': self.player.role == 'authority'
        }

    def before_next_page(self):
        self.player.set_payoffs()

    pass

class Subordinte(Page):
    def is_displayed(self):
        return self.player.role == 'subordinate'

    form_model = models.Player
    form_fields = ['mychoice']
    def vars_for_template(self):
        return {
            'round': self.round_number,
            'authority': self.player.role == 'authority'
        }
    def before_next_page(self):
        self.player.set_payoffs()

    pass

class Results(Page):

    pass

class ChangeRole(Page):
    def is_displayed(self):
        return self.round_number == 21

    def vars_for_template(self):
        return {
            'role': self.player.role
        }

    pass


page_sequence = [
    ChangeRole,
    Introduction,
    Payement_Info,
    VSComputer,
    Authority,
    Subordinte,
    Results
]
