from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.employment import Employment
from backend.utils.db_connect import db
from backend.app.forms.employment_form import EmploymentForm

employment_bp = Blueprint('employment', __name__, url_prefix='/employment')

@employment_bp.route('/list')
def list_employments():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    employments = Employment.query.all()
    return render_template('employment_list.html', employments=employments)

@employment_bp.route('/view/<int:EID>')
def view_employment(EID):
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('employment.list_employments'))
    employment = Employment.query.get_or_404(EID)
    return render_template('employment_view.html', employment=employment)

@employment_bp.route('/add', methods=['GET', 'POST'])
def add_employment():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('employment.list_employments'))
    form = EmploymentForm()
    if form.validate_on_submit():
        new_employment = Employment(**{f: getattr(form, f).data for f in form.data if f not in ('csrf_token', 'submit')})
        db.session.add(new_employment)
        db.session.commit()
        flash('Employment added successfully', 'success')
        return redirect(url_for('employment.list_employments'))
    return render_template('employment_form.html', form=form)

@employment_bp.route('/edit/<int:EID>', methods=['GET', 'POST'])
def edit_employment(EID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('employment.list_employments'))
    employment = Employment.query.get_or_404(EID)
    form = EmploymentForm(obj=employment)
    if form.validate_on_submit():
        form.populate_obj(employment)
        db.session.commit()
        flash('Employment updated successfully', 'success')
        return redirect(url_for('employment.list_employments'))
    return render_template('employment_form.html', form=form)

@employment_bp.route('/delete/<int:EID>', methods=['POST'])
def delete_employment(EID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('employment.list_employments'))
    employment = Employment.query.get_or_404(EID)
    db.session.delete(employment)
    db.session.commit()
    flash('Employment deleted successfully', 'success')
    return redirect(url_for('employment.list_employments'))
