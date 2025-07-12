from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.user import User
from backend.app.forms.login_form import LoginForm

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(UID=form.UID.data).first()
        if user is None:
            flash('User not found', 'danger')
        elif not user.check_password(form.password.data):
            flash('Invalid password', 'danger')
        else:
            session['user_id'] = user.UID
            session['perms'] = {
                'view': user.viewPriveledgeYN,
                'insert': user.insertPriveledgeYN,
                'update': user.updatePriveledgeYN,
                'delete': user.deletePriveledgeYN
            }
            flash('Login successful', 'success')
            return redirect(url_for('alumni.list_alumni'))
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out', 'info')
    return redirect(url_for('auth_bp.login'))
