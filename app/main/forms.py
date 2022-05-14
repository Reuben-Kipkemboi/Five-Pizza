from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField, SubmitField
from wtforms.validators import DataRequired

# #User update profile
# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Briefly describe yourself.',validators = [DataRequired()])
#     submit = SubmitField('Submit')

class PizzaForm(FlaskForm):
    name = StringField('Pizza Type ', validators=[DataRequired()])
    price = TextAreaField('pizza Price.',validators = [DataRequired()])
    description = TextAreaField('Enter Pizza Description', validators=[DataRequired()])
    
    category = SelectField('Category', choices=[('Large','large'),('Medium' ,'Medium'),('Small','Small')], validators=[DataRequired()])
    submit = SubmitField('Add pizza')

# class CommentForm(FlaskForm):
#     comment_content = TextAreaField('Provide feedback/Comments', validators=[DataRequired()])
#     submit = SubmitField('Add Comment')


class PitchOrderForm(FlaskForm):
    category = SelectField('Choose pizza type',choices = [('Cheese Pizza','Cheese Pizza'),('Veggie Pizza','Veggie Pizza'),('Pepperoni Pizza','Pepperoni Pizza'),('Meat Pizza','Meat Pizza'),('Margherita Pizza','Margherita Pizza'),(' Hawaiian Pizza ',' Hawaiian Pizza ')]) 
    name = TextAreaField('Your Name')
    title = TextAreaField('title')
    context = TextAreaField('Pitch itself')
    submit = SubmitField('Submit')