from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from random import randint


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/roll')
def roll():
    attributes = []
    for _ in range(6):
        rolls = [randint(1, 6) for _ in range(4)]
        rolls.sort()
        rolls.pop(0)
        attributes.append(sum(rolls))
    return ' '.join((str(x) for x in attributes))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpendID="{}", remember_me={}'.format(
            form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

