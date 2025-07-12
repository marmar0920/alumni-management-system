from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from backend.models.newsletter import Newsletter
from backend.utils.db_connect import db
from backend.app.forms.newsletter_form import NewsletterForm

newsletter_bp = Blueprint('newsletter', __name__, url_prefix='/newsletter')

@newsletter_bp.route('/list')
def list_newsletters():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('auth_bp.login'))
    newsletters = Newsletter.query.all()
    return render_template('newsletter_list.html', newsletters=newsletters)

@newsletter_bp.route('/view/<int:NID>')
def view_newsletter(NID):
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('newsletter.list_newsletters'))
    newsletter = Newsletter.query.get_or_404(NID)
    return render_template('newsletter_view.html', newsletter=newsletter)

@newsletter_bp.route('/add', methods=['GET', 'POST'])
def add_newsletter():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Not allowed', 'warning')
        return redirect(url_for('newsletter.list_newsletters'))
    form = NewsletterForm()
    if form.validate_on_submit():
        new_newsletter = Newsletter(**{f: getattr(form, f).data for f in form.data if f not in ('csrf_token', 'submit')})
        db.session.add(new_newsletter)
        db.session.commit()
        flash('Newsletter added successfully', 'success')
        return redirect(url_for('newsletter.list_newsletters'))
    return render_template('newsletter_form.html', form=form)

@newsletter_bp.route('/edit/<int:NID>', methods=['GET', 'POST'])
def edit_newsletter(NID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('newsletter.list_newsletters'))
    newsletter = Newsletter.query.get_or_404(NID)
    form = NewsletterForm(obj=newsletter)
    if form.validate_on_submit():
        form.populate_obj(newsletter)
        db.session.commit()
        flash('Newsletter updated successfully', 'success')
        return redirect(url_for('newsletter.list_newsletters'))
    return render_template('newsletter_form.html', form=form)

@newsletter_bp.route('/delete/<int:NID>', methods=['POST'])
def delete_newsletter(NID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'warning')
        return redirect(url_for('newsletter.list_newsletters'))
    newsletter = Newsletter.query.get_or_404(NID)
    db.session.delete(newsletter)
    db.session.commit()
    flash('Newsletter deleted successfully', 'success')
    return redirect(url_for('newsletter.list_newsletters'))
