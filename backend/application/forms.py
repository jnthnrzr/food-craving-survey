"""forms.py - Definitions of the various forms needed for the project."""
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, NumberRange


class InputForm(FlaskForm):
    """A form for the input_participant number input."""
    not_number = "The input was not valid. Please enter a whole number."
    too_low = "The input was not valid. The number must be more than 0."
    number = IntegerField(validators=[DataRequired(message=not_number),
                                      NumberRange(min=1, message=too_low)])


class PictureForm(FlaskForm):
    """A form for the picture scoring pages."""
    rating = IntegerRangeField('Rating', default=0)
    submit = SubmitField('Next')
