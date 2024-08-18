from flask import render_template, redirect, url_for, flash, request, flash, session
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from functools import wraps
from app.blueprints.auth.forms import LoginForm
from . import auth_bp
from ...models import Membro


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        membro = Membro.query.filter_by(email=form.email.data).first()
        if membro and check_password_hash(membro.password, form.password.data):
            session['user_id'] = membro.id
            session['user_email'] = membro.email
            flash('Login eseguito con successo!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Email o password non corretti', 'danger')
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    flash('Logout eseguito con successo!', 'success')
    return redirect(url_for('auth.login'))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Devi effettuare il login per accedere a questa pagina.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
