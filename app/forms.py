""" forms.py provides a class for each web form """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from outpost_calc import valid_cards_syntax

class LoginForm(FlaskForm):
    """ A regular login form """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CardsForm(FlaskForm):
    """ Form for entering the list of cards """
    cards = StringField('Enter card values separated by periods:', validators=[DataRequired()])
    submit = SubmitField('Calculate Totals')

    def validate_cards(self, cards):
        """ use validator from outpost_calc to verify user input """
        error_msg = valid_cards_syntax(cards.data)
        if error_msg is not None:
            raise ValidationError(error_msg)
