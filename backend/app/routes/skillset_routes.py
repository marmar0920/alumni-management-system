from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.app.forms import skillset_form
from backend.models import skillset
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
    form = SkillsetForm()
    if form.validate_on_submit():
        new_skill = Skillset(
            alumniID=form.alumniID.data,
            skill=form.skill.data,
            proficiency=form.proficiency.data,
            description=form.description.data
        )
        db.session.add(new_skill)
        db.session.commit()
        flash('Skill added successfully!', 'success')
        return redirect(url_for('alumni.edit_alumni', alumniID=form.alumniID.data))
    return render_template('skillset_form.html', form=form)

@skillset_bp.route('/edit/<int:SID>', methods=['GET', 'POST'])
def edit_skill(SID):
    skill = skillset_form.query.get_or_404(SID)
    form = SkillsetForm(obj=skill)
    if form.validate_on_submit():
        skill.skill = form.skill.data
        skill.proficiency = form.proficiency.data
        skill.description = form.description.data
        db.session.commit()
        flash('Skill updated successfully!', 'success')
        return redirect(url_for('alumni.edit_alumni', alumniID=skill.alumniID))
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
