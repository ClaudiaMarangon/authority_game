from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




class ChoiceP1(Page):
    form_model = models.Player
    form_fields = ['choicep1', 'p2pay']
    pass

class Results(Page):
    pass


page_sequence = [
    ChoiceP1,
    Results,
]
