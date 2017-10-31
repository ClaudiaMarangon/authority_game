from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=100
    )
    gender = models.CharField(
        verbose_name='What is your gender?',
        choices=['Female', 'Male'],
        widget=widgets.RadioSelect
    )
    economics = models.CharField(
        verbose_name='Are you studying economics?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )
    game_theory = models.CharField(
        verbose_name='Did you complete a Game Theory course at your institution?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )
    grade_gt = models.PositiveIntegerField(
        verbose_name='If yes, what grade did you receive?',
        initial=0,
        max=31,
        min=0
    )
    rules = models.PositiveIntegerField(
        verbose_name='This person believes that people should follow rules at all times, even when no-one'
                     'is watching. Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    others_op = models.PositiveIntegerField(
        verbose_name='It is important to this person to always behave well and avoid doing anything people say is wrong.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    polite = models.PositiveIntegerField(
        verbose_name='It is important for this person to be polite to other people all the time and never annoy others.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    satisfaction = models.PositiveIntegerField(
        verbose_name='This person believes that people should be satisfied with what they have.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    religious = models.PositiveIntegerField(
        verbose_name='Religious belief is important to this person and tries hard to do what religion requires.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    tradition = models.PositiveIntegerField(
        verbose_name='This person thinks it is best to do things in traditional ways and keep up the customs he has learned.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    planning = models.PositiveIntegerField(
        verbose_name='It is important to this person to make own plans and decide what to do.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    interest = models.PositiveIntegerField(
        verbose_name='This person thinks it is important to be interested in things and try to understand all sorts of things.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    independent = models.PositiveIntegerField(
        verbose_name='It is important to this person to be independent and rely on himself/herself.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very much like me'],
            [2, 'Somewhat like me'],
            [3, 'Little like me'],
            [4, 'Not like me at all'],
        ],
        widget = widgets.RadioSelect
    )
    risk_aversion = models.PositiveIntegerField(
        verbose_name='It is important to this person to be independent and rely on himself/herself.'
                     ' Think about how much this person is or is not like you.',
        choices=[
            [1, 'Very willing to take risks'],
            [2, 'Somewhat willing to take risks'],
            [3, 'Somewhat against taking risks'],
            [4, 'Very much against taking risks'],
        ],
        widget = widgets.RadioSelect
    )
    pass
