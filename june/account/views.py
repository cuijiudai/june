from flask import Blueprint
from flask import render_template
from flask import request
from .models import db, Member
from .helpers import login, logout

app = Blueprint('account', __name__)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    user = Member.query.filter_by(id=1).first()
    login(user)
    return 'ok'


@app.route('/signout')
def signout():
    logout()
    return 'signout'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = Member(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
    return render_template('account/signup.html')
