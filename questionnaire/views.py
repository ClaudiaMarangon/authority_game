from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Survey1(Page):
    form_model = models.Player
    form_fields = ['age', 'gender', 'economics', 'game_theory', 'grade_gt']
    pass

class Survey2(Page):
    form_model = models.Player
    form_fields = ['rules', 'others_op', 'polite', 'satisfaction', 'religious', 'tradition', 'planning', 'interest', 'independent']
    pass

class Survey3(Page):
    form_model = models.Player
    form_fields = ['risk_aversion']
    pass

page_sequence = [
    Survey1,
    Survey2,
    Survey3,
]