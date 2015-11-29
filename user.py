#!/usr/bin/python
from flask import Flask, render_template, request, flash
from flask import Flask
from forms import UserCreationForm , UserDeletion, UserUpdateForm
from lib.createUser import *
from lib.updateUser import *
from lib.deleteUser import *
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
      return render_template('create_user.html', form=form)
    else:
      
      print "Name Is %s" %(form.username.data)
      print "Shell Is %s" %(form.sudo.data)
      print ('hello i am here1')
      


      f1=str(form.name.data)
      f2=str(form.username.data)
      f3=str(form.shelltype.data)
      f4=str(form.homefolder.data)
      f5=str(form.password.data)
      f6=str(form.sudo.data)
      print ('hello i am here2')

#      print f1 , f2 , f3, f4 ,f5,f6
      print ('hello i am here3')	 
      s=createUser(f1,f2,f3,f4,f5,f6)
      print ('helllo i am here 4')
      return render_template('success.html' , result=s)

  else:    
      return render_template('create_user.html', form=form ,page_title = 'create User Form')



@app.route('/update', methods=['GET', 'POST'])
def update():
  form = UserUpdateForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('update_user.html', form=form)
    else:

      print "Name Is %s" %(form.username.data)
      print "Shell Is %s" %(form.sudo.data)
      print ('hello i am here1')



      f1=str(form.name.data)
      f2=str(form.username.data)
      f3=str(form.shelltype.data)
      f4=str(form.homefolder.data)
      f5=str(form.password.data)
      f6=str(form.sudo.data)
      print ('hello i am here2')

#      print f1 , f2 , f3, f4 ,f5,f6
      print ('hello i am here3')
      u=updateUser(f1,f2,f3,f4,f5,f6)
      print ('helllo i am here 4')
      return render_template('success.html', result=u)




  else:
    return render_template('update_user.html', form=form ,page_title = 'Update User Form')



@app.route('/delete',methods=['GET','POST'])
def delete():
  form = UserDeletion()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('delete_user.html', form=form)
    else:

      print ('hello i am here1')



      f7=str(form.username.data)
      print ('hello i am here2')

#      print f1 , f2 , f3, f4 ,f5,f6
      print ('hello i am here3')
      d=deleteUser(f7)
      print ('helllo i am here 4')
      return render_template('success.html', result=d)




  elif request.method == 'GET':
    return render_template('delete_user.html', form=form ,page_title = 'Delete User Form')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

