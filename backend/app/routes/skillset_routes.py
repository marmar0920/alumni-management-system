from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.skillset import Skillset
from backend.utils.db_connect import db
from backend.app.forms.skillset_form import SkillsetForm

skillset_bp = Blueprint('skillset', __name__, url_prefix='/skillset')

@skillset_bp.route('/list')
def list_skillsets():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    skillsets = Skillset.query.all()
    return render_template('skillset_list.html', skillsets=skillsets)

@skillset_bp.route('/view/<int:SID>')
def view_skillset(SID):
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('skillset.list_skillsets'))
    skillset = Skillset.query.get_or_404(SID)
    return render_template('skillset_view.html', skillset=skillset)

@skillset_bp.route('/add', methods=['GET', 'POST'])
def add_skillset():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('skillset.list_skillsets'))
    form = SkillsetForm()
    if form.validate_on_submit():
        new_skillset = Skillset(**{f: getattr(form, f).data for f in form.data if f != 'csrf_token'})
        db.session.add(new_skillset)
        db.session.commit()
        flash('Skillset added successfully', 'success')
        return redirect(url_for('skillset.list_skillsets'))
    return render_template('skillset_form.html', form=form)

@skillset_bp.route('/edit/<int:SID>', methods=['GET', 'POST'])
def edit_skillset(SID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('skillset.list_skillsets'))
    skillset = Skillset.query.get_or_404(SID)
    form = SkillsetForm(obj=skillset)
    if form.validate_on_submit():
        form.populate_obj(skillset)
        db.session.commit()
        flash('Skillset updated successfully', 'success')
        return redirect(url_for('skillset.list_skillsets'))
    return render_template('skillset_form.html', form=form)

@skillset_bp.route('/delete/<int:SID>', methods=['POST'])
def delete_skillset(SID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('skillset.list_skillsets'))
    skillset = Skillset.query.get_or_404(SID)
    db.session.delete(skillset)
    db.session.commit()
    flash('Skillset deleted successfully', 'success')
    return redirect(url_for('skillset.list_skillsets'))
