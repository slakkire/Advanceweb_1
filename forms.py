from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField("Enter Student Name: ")
    grade = IntegerField("Enter Student Grade: ")
    submit = SubmitField("Add Student Detail")

class DelForm(FlaskForm):

    id = IntegerField("Enter Id no of remove stduent details: ")
    submit = SubmitField("Remove Student Detail")

class AddFatherForm(FlaskForm):
    name = StringField("Enter Student Father Name: ")
    stu_id = IntegerField("Enter Student Id:")
    submit = SubmitField("Add Father Name")