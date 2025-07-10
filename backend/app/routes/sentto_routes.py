from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.sentto import SentTo
from backend.utils.db_connect import db
from backend.app.forms.sentto_form import SentToForm

sentto_bp = Blueprint('sentto', __name__, url_prefix='/sentto')

@sentto_bp.route('/list')
def list_sentto():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    sent_entries = SentTo.query.all()
    return render_template('sentto_list.html', sent_entries=sent_entries)

@sentto_bp.route('/add', methods=['GET', 'POST'])
def add_sentto():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('sentto.list_sentto'))
    form = SentToForm()
    if form.validate_on_submit():
        new_entry = SentTo(**{f: getattr(form, f).data for f in form.data if f != 'csrf_token'})
        db.session.add(new_entry)
        db.session.commit()
        flash('SentTo entry added successfully', 'success')
        return redirect(url_for('sentto.list_sentto'))
    return render_template('sentto_form.html', form=form)

@sentto_bp.route('/delete/<int:alumniID>/<int:NID>', methods=['POST'])
def delete_sentto(alumniID, NID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('sentto.list_sentto'))
    entry = SentTo.query.get_or_404((alumniID, NID))
    db.session.delete(entry)
    db.session.commit()
    flash('SentTo entry deleted successfully', 'success')
    return redirect(url_for('sentto.list_sentto'))
