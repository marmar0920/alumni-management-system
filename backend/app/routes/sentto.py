from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.models.sentto import SentTo
from backend.utils.db_connect import db
from backend.app.forms.sentto_form import SentToForm

sentto_bp = Blueprint('sentto_bp', __name__, url_prefix='/sentto')

@sentto_bp.route('/list')
def list_sentto():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('auth_bp.login'))
    sent_entries = SentTo.query.all()
    return render_template('sentto_list.html', sent_entries=sent_entries)

@sentto_bp.route('/add', methods=['GET', 'POST'])
def add_sentto():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('sentto_bp.list_sentto'))
    form = SentToForm()
    if form.validate_on_submit():
        new_entry = SentTo(**form.data)
        db.session.add(new_entry)
        db.session.commit()
        flash('SentTo entry added.', 'success')
        return redirect(url_for('sentto_bp.list_sentto'))
    return render_template('sentto_form.html', form=form)

@sentto_bp.route('/delete/<int:alumniID>/<int:NID>', methods=['POST'])
def delete_sentto(alumniID, NID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('sentto_bp.list_sentto'))
    entry = SentTo.query.get_or_404((alumniID, NID))
    db.session.delete(entry)
    db.session.commit()
    flash('SentTo entry deleted.', 'success')
    return redirect(url_for('sentto_bp.list_sentto'))
