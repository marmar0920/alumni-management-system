from flask import Blueprint, render_template, redirect, url_for, session, flash
from backend.app.forms.login_form import LoginForm
from backend.models.user import User
from backend.utils.db_connect import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.UID.data)
        if user and user.check_password(form.password.data):
            session['user_id'] = user.UID
            session['perms'] = {
                'view': user.viewPriveledgeYN == 'Y',
                'insert': user.insertPriveledgeYN == 'Y',
                'update': user.updatePriveledgeYN == 'Y',
                'delete': user.deletePriveledgeYN == 'Y'
            }
            return redirect(url_for('alumni.list'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
