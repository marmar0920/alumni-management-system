from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.address import Address
from backend.models.alumni import Alumni
from backend.app.forms.address_form import AddressForm
from backend.utils.db_connect import db

address_bp = Blueprint('address', __name__, url_prefix='/address')

@address_bp.route('/list')
def list_addresses():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    addresses = Address.query.all()
    return render_template('address_list.html', addresses=addresses)

@address_bp.route('/view/<int:addressID>')
def view_address(addressID):
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('address.list_addresses'))
    address = Address.query.get_or_404(addressID)
    return render_template('address_view.html', address=address)

@address_bp.route('/add/<int:alumniID>', methods=['GET', 'POST'])
def add_address(alumniID):
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('address.list_addresses'))
        
    alumniID = request.args.get('alumniID', type=int)
    form = AddressForm()

    if alumniID:
        form.alumniID.data = alumniID

    if form.validate_on_submit():
        if form.primaryYN.data == 'Y':
            Address.query.filter_by(alumniID=form.alumniID.data, primaryYN='Y').update({'primaryYN': 'N'})

        new_address = Address(
            alumniID=form.alumniID.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            zipCode=form.zipCode.data,
            activeYN=form.activeYN.data,
            primaryYN=form.primaryYN.data
        )
        db.session.add(new_address)
        db.session.commit()
        flash('Address added successfully', 'success')
        return redirect(url_for('alumni.edit_alumni', alumniID=alumniID))
    
    return render_template('address_form.html', form=form)

@address_bp.route('/edit/<int:addressID>', methods=['GET', 'POST'])
def edit_address(addressID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('address.list_addresses'))
    address = Address.query.get_or_404(addressID)
    form = AddressForm(obj=address)
    if form.validate_on_submit():
        form.populate_obj(address)
        db.session.commit()
        flash('Address updated successfully', 'success')
        return redirect(url_for('address.view_address', addressID=addressID))
    return render_template('address_form.html', form=form)

@address_bp.route('/delete/<int:addressID>', methods=['POST'])
def delete_address(addressID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('address.list_addresses'))
    address = Address.query.get_or_404(addressID)
    alumniID = address.alumniID
    db.session.delete(address)
    db.session.commit()
    flash('Address deleted successfully', 'success')
    return redirect(url_for('alumni.edit_alumni', alumniID=alumniID))
    db.session.commit()
    flash('Alumni deleted successfully', 'success')     