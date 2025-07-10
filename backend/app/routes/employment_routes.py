from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.models.employment import Employment
from backend.utils.db_connect import db
from backend.app.forms.employment_form import EmploymentForm

employment_bp = Blueprint('employment_bp', __name__, url_prefix='/employment')

@employment_bp.route('/list')
def list_employments():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('auth_bp.login'))
    jobs = Employment.query.all()
    return render_template('employment_list.html', jobs=jobs)

@employment_bp.route('/view/<int:EID>')
def view_employment(EID):
    job = Employment.query.get_or_404(EID)
    return render_template('employment_view.html', job=job)

@employment_bp.route('/add', methods=['GET', 'POST'])
def add_employment():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('employment_bp.list_employments'))
    form = EmploymentForm()
    if form.validate_on_submit():
        new_job = Employment(**form.data)
        db.session.add(new_job)
        db.session.commit()
        flash('Employment added.', 'success')
        return redirect(url_for('employment_bp.list_employments'))
    return render_template('employment_form.html', form=form)

@employment_bp.route('/edit/<int:EID>', methods=['GET', 'POST'])
def edit_employment(EID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('employment_bp.list_employments'))
    job = Employment.query.get_or_404(EID)
    form = EmploymentForm(obj=job)
    if form.validate_on_submit():
        form.populate_obj(job)
        db.session.commit()
        flash('Employment updated.', 'success')
        return redirect(url_for('employment_bp.view_employment', EID=job.EID))
    return render_template('employment_form.html', form=form)

@employment_bp.route('/delete/<int:EID>', methods=['POST'])
def delete_employment(EID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('employment_bp.list_employments'))
    job = Employment.query.get_or_404(EID)
    db.session.delete(job)
    db.session.commit()
    flash('Employment deleted.', 'success')
    return redirect(url_for('employment_bp.list_employments'))
