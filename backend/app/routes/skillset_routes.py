from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.models.skillset import Skillset
from backend.utils.db_connect import db
from backend.app.forms.skillset_form import SkillsetForm

skillset_bp = Blueprint('skillset_bp', __name__, url_prefix='/skillset')

@skillset_bp.route('/list')
def list_skillsets():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('auth_bp.login'))
    skills = Skillset.query.all()
    return render_template('skillset_list.html', skills=skills)

@skillset_bp.route('/view/<int:SID>')
def view_skillset(SID):
    skill = Skillset.query.get_or_404(SID)
    return render_template('skillset_view.html', skill=skill)

@skillset_bp.route('/add', methods=['GET', 'POST'])
def add_skillset():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('skillset_bp.list_skillsets'))
    form = SkillsetForm()
    if form.validate_on_submit():
        new_skill = Skillset(**form.data)
        db.session.add(new_skill)
        db.session.commit()
        flash('Skillset added.', 'success')
        return redirect(url_for('skillset_bp.list_skillsets'))
    return render_template('skillset_form.html', form=form)

@skillset_bp.route('/edit/<int:SID>', methods=['GET', 'POST'])
def edit_skillset(SID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('skillset_bp.list_skillsets'))
    skill = Skillset.query.get_or_404(SID)
    form = SkillsetForm(obj=skill)
    if form.validate_on_submit():
        form.populate_obj(skill)
        db.session.commit()
        flash('Skillset updated.', 'success')
        return redirect(url_for('skillset_bp.view_skillset', SID=skill.SID))
    return render_template('skillset_form.html', form=form)

@skillset_bp.route('/delete/<int:SID>', methods=['POST'])
def delete_skillset(SID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('skillset_bp.list_skillsets'))
    skill = Skillset.query.get_or_404(SID)
    db.session.delete(skill)
    db.session.commit()
    flash('Skillset deleted.', 'success')
    return redirect(url_for('skillset_bp.list_skillsets'))
