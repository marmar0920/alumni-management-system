from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.alumni import Alumni
from backend.app.forms.alumni_form import AlumniForm
from backend.utils.db_connect import db

alumni_bp = Blueprint('alumni', __name__, url_prefix='/alumni')

@alumni_bp.route('/list')
def list_alumni():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    alumni = Alumni.query.all()
    return render_template('alumni_list.html', alumni=alumni)

@alumni_bp.route('/add', methods=['GET', 'POST'])
def add_alumni():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('alumni.list_alumni'))
    form = AlumniForm()
    if form.validate_on_submit():
        new_alumnus = Alumni(**{
            f: getattr(form, f).data
            for f in form.data
            if f not in ('csrf_token', 'submit')
        })
        db.session.add(new_alumnus)
        db.session.commit()
        flash('Added successfully', 'success')
        return redirect(url_for('alumni.list_alumni'))
    return render_template('alumni_form.html', form=form)
