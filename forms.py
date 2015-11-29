from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError,BooleanField,PasswordField
 
class UserCreationForm(Form):
  name = TextField("Name",  [validators.Required()])
  username = TextField("UserName",  [validators.Required()])
  shelltype = TextField("ShellType",  [validators.Required()])
  homefolder = TextField("HomeFolder",  [validators.Required()])
  password = PasswordField("UserPassword", [validators.Required(),validators.EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField("RepeatPassword",[validators.Required()])
  sudo = BooleanField("Sudo", default=False)
  submit = SubmitField("Submit")

