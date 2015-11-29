#!/usr/bin/python
from flask import Flask, render_template, request, flash
from flask import Flask
from forms import UserCreationForm
#config.from_object('config')
app = Flask(__name__)
app.secret_key = 'kjshdkasi7374628jvjvjvv'
@app.route('/')
def hello_world():
     return render_template('welcome.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
  form = UserCreationForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('create_user1.html', form=form)
    else:
      
      print "Name Is %s" %(form.username.data)
      print "Shell Is %s" %(form.sudo.data)
      return 'Form posted.'




  elif request.method == 'GET':
    return render_template('create_user1.html', form=form ,page_title = 'Create User Form')



if __name__ == '__main__':
    app.run(debug = True)

