from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from . import auth_bp
from ...models import Membro

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Trova l'utente nel database
        user = Membro.query.filter_by(email=email).first()

        # Verifica la password
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
