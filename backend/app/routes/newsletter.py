from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.models.newsletter import Newsletter
from backend.utils.db_connect import db
from backend.app.forms.newsletter_form import NewsletterForm

newsletter_bp = Blueprint('newsletter_bp', __name__, url_prefix='/newsletter')

@newsletter_bp.route('/list')
def list_newsletters():
    if session.get('perms', {}).get('view') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('auth_bp.login'))
    newsletters = Newsletter.query.all()
    return render_template('newsletter_list.html', newsletters=newsletters)

@newsletter_bp.route('/view/<int:NID>')
def view_newsletter(NID):
    newsletter = Newsletter.query.get_or_404(NID)
    return render_template('newsletter_view.html', newsletter=newsletter)

@newsletter_bp.route('/add', methods=['GET', 'POST'])
def add_newsletter():
    if session.get('perms', {}).get('insert') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('newsletter_bp.list_newsletters'))
    form = NewsletterForm()
    if form.validate_on_submit():
        new_news = Newsletter(**form.data)
        db.session.add(new_news)
        db.session.commit()
        flash('Newsletter created.', 'success')
        return redirect(url_for('newsletter_bp.list_newsletters'))
    return render_template('newsletter_form.html', form=form)

@newsletter_bp.route('/edit/<int:NID>', methods=['GET', 'POST'])
def edit_newsletter(NID):
    if session.get('perms', {}).get('update') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('newsletter_bp.list_newsletters'))
    newsletter = Newsletter.query.get_or_404(NID)
    form = NewsletterForm(obj=newsletter)
    if form.validate_on_submit():
        form.populate_obj(newsletter)
        db.session.commit()
        flash('Newsletter updated.', 'success')
        return redirect(url_for('newsletter_bp.view_newsletter', NID=newsletter.NID))
    return render_template('newsletter_form.html', form=form)

@newsletter_bp.route('/delete/<int:NID>', methods=['POST'])
def delete_newsletter(NID):
    if session.get('perms', {}).get('delete') != 'Y':
        flash('Unauthorized', 'danger')
        return redirect(url_for('newsletter_bp.list_newsletters'))
    newsletter = Newsletter.query.get_or_404(NID)
    db.session.delete(newsletter)
    db.session.commit()
    flash('Newsletter deleted.', 'success')
    return redirect(url_for('newsletter_bp.list_newsletters'))
