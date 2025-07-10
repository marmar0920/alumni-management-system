from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.degree import Degree
from backend.utils.db_connect import db
from backend.app.forms.degree_form import DegreeForm

degree_bp = Blueprint('degree', __name__, url_prefix='/degree')

@degree_bp.route('/list')
def list_degrees():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    degrees = Degree.query.all()
    return render_template('degree_list.html', degrees=degrees)

@degree_bp.route('/view/<int:degreeID>')
def view_degree(degreeID):
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('degree.list_degrees'))
    degree = Degree.query.get_or_404(degreeID)
    return render_template('degree_view.html', degree=degree)

@degree_bp.route('/add', methods=['GET', 'POST'])
def add_degree():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('degree.list_degrees'))
    form = DegreeForm()
    if form.validate_on_submit():
        new_degree = Degree(**{f: getattr(form, f).data for f in form.data if f != 'csrf_token'})
        db.session.add(new_degree)
        db.session.commit()
        flash('Degree added successfully', 'success')
        return redirect(url_for('degree.list_degrees'))
    return render_template('degree_form.html', form=form)

@degree_bp.route('/edit/<int:degreeID>', methods=['GET', 'POST'])
def edit_degree(degreeID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('degree.list_degrees'))
    degree = Degree.query.get_or_404(degreeID)
    form = DegreeForm(obj=degree)
    if form.validate_on_submit():
        form.populate_obj(degree)
        db.session.commit()
        flash('Degree updated successfully', 'success')
        return redirect(url_for('degree.list_degrees'))
    return render_template('degree_form.html', form=form)

@degree_bp.route('/delete/<int:degreeID>', methods=['POST'])
def delete_degree(degreeID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('degree.list_degrees'))
    degree = Degree.query.get_or_404(degreeID)
    db.session.delete(degree)
    db.session.commit()
    flash('Degree deleted successfully', 'success')
    return redirect(url_for('degree.list_degrees'))
