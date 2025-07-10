from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.alumni import Alumni
from backend.app.forms.alumni_form import AlumniForm
from backend.utils.db_connect import db

alumni_bp = Blueprint('alumni', __name__, url_prefix='/alumni')

@alumni_bp.route('/list')
def list():
    if not session.get('perms', {}).get('view'):
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth.login'))
    data = Alumni.query.all()
    return render_template('alumni_list.html', alumni=data)

@alumni_bp.route('/add', methods=['GET','POST'])
def add():
    if not session.get('perms', {}).get('insert'):
        flash('Not allowed', 'warning')
        return redirect(url_for('alumni.list'))
    form = AlumniForm()
    if form.validate_on_submit():
        obj = Alumni(**{f: getattr(form, f).data for f in form.data if f != 'csrf_token'})
        db.session.add(obj)
        db.session.commit()
        flash('Added successfully', 'success')
        return redirect(url_for('alumni.list'))
    return render_template('alumni_form.html', form=form)
