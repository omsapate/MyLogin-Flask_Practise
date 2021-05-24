from flask.helpers import url_for
from werkzeug.utils import redirect
from application import app
from flask import render_template, request, flash
from application.models import User



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.objects(email=email).first()
        

        if user and user.get_password(password):
            flash('Logged in successfully')
            return redirect(url_for('home'))
        else:
            flash('Something is wrong, try again.')
    return render_template('login.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user_id     = User.objects.count()
        user_id     += 1

        user = User(user_id = user_id, name=name, email = email)
        user.set_password(password)
        user.save()
        flash('Registered Successfully !! Login Now.')
        return redirect(url_for('login'))
    return render_template('register.html')