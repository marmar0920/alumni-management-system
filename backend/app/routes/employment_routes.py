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
def add_employment(alumniID):
    # Make sure user has permission to insert
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('employment.list_employments'))

    alumniID = request.args.get('alumniID', type=int)
    form = EmploymentForm()

   
    if alumniID:
        form.alumniID.data = alumniID

    if form.validate_on_submit():
        if form.currentYN.data == 'Y':
            Employment.query.filter_by(alumniID=form.alumniID.data, currentYN='Y').update({'currentYN': 'N'})

        new_employment = Employment(
            alumniID=form.alumniID.data,
            company=form.company.data,
            city=form.city.data,
            state=form.state.data,
            zip=form.zip.data,
            jobTitle=form.jobTitle.data,
            startDate=form.startDate.data,
            endDate=form.endDate.data,
            currentYN=form.currentYN.data,
            
        )

        db.session.add(new_employment)
        db.session.commit()
        flash('Employment added successfully', 'success')
        return redirect(url_for('alumni.edit_alumni', alumniID=form.alumniID.data))

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
        return redirect(url_for('alumni.edit_alumni', alumniID=employment.alumniID))
    return render_template('employment_form.html', form=form)

@employment_bp.route('/delete/<int:EID>', methods=['POST'])
def delete_employment(EID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('employment.list_employments'))
    employment = Employment.query.get_or_404(EID)
    alumniID = employment.alumniID
    db.session.delete(employment)
    db.session.commit()
    flash('Employment deleted successfully', 'success')
    return redirect(url_for('alumni.edit_alumni', alumniID=alumniID))
    db.session.commit()
    