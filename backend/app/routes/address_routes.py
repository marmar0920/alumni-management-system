from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.address import Address
from backend.utils.db_connect import db
from backend.app.forms.address_form import AddressForm

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

@address_bp.route('/add', methods=['GET', 'POST'])
def add_address():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('address.list_addresses'))
    form = AddressForm()
    if form.validate_on_submit():
        new_address = Address(**{
            f: getattr(form, f).data
            for f in form.data
            if f not in ('csrf_token', 'submit')
        })
        db.session.add(new_address)
        db.session.commit()
        flash('Address added successfully', 'success')
        return redirect(url_for('address.list_addresses'))
    return render_template('address_form.html', form=form)

@address_bp.route('/edit/<int:addressID>', methods=['GET', 'POST'])
def edit_address(addressID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('address.list_addresses'))
    address = Address.query.get_or_404(addressID)
    form = AddressForm(obj=address)
    if form.validate_on_submit():
        for field in form.data:
            if field not in ('csrf_token', 'submit'):
                setattr(address, field, getattr(form, field).data)
        db.session.commit()
        flash('Address updated successfully', 'success')
        return redirect(url_for('address.list_addresses'))
    return render_template('address_form.html', form=form)

@address_bp.route('/delete/<int:addressID>', methods=['POST'])
def delete_address(addressID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('address.list_addresses'))
    address = Address.query.get_or_404(addressID)
    db.session.delete(address)
    db.session.commit()
    flash('Address deleted successfully', 'success')
    return redirect(url_for('address.list_addresses'))
