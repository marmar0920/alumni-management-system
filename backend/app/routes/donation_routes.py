from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.donation import Donation
from backend.utils.db_connect import db
from backend.app.forms.donation_form import DonationForm

donation_bp = Blueprint('donation', __name__, url_prefix='/donation')

@donation_bp.route('/list')
def list_donations():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    donations = Donation.query.all()
    return render_template('donation_list.html', donations=donations)

@donation_bp.route('/view/<int:donationID>')
def view_donation(donationID):
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('donation.list_donations'))
    donation = Donation.query.get_or_404(donationID)
    return render_template('donation_view.html', donation=donation)

@donation_bp.route('/add', methods=['GET', 'POST'])
def add_donation(alumniID):
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('alumni.edit_alumni', alumniID=alumniID))
    form = DonationForm()
    if request.method == 'GET':
        form.alumniID.data = alumniID  # Pre-populate alumniID in the form
    if form.validate_on_submit():
        new_donation = Donation(**{
            f: getattr(form, f).data 
            for f in form.data 
            if f not in ('csrf_token', 'submit')
        })
        db.session.add(new_donation)
        db.session.commit()
        flash('Donation added successfully', 'success')
        return redirect(url_for('alumni.edit_alumni', alumniID=alumniID))
    return render_template('donation_form.html', form=form)
@donation_bp.route('/edit/<int:donationID>', methods=['GET', 'POST'])
def edit_donation(donationID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('donation.list_donations'))
    donation = Donation.query.get_or_404(donationID)
    form = DonationForm(obj=donation)
    if form.validate_on_submit():
        form.populate_obj(donation)
        db.session.commit()
        flash('Donation updated successfully', 'success')
        return redirect(url_for('donation.list_donations'))
    return render_template('donation_form.html', form=form)

@donation_bp.route('/delete/<int:donationID>', methods=['POST'])
def delete_donation(donationID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('donation.list_donations'))
    donation = Donation.query.get_or_404(donationID)
    db.session.delete(donation)
    db.session.commit()
    flash('Donation deleted successfully', 'success')
    return redirect(url_for('donation.list_donations'))
