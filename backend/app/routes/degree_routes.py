degree_bp = Blueprint('degree_bp', __name__, url_prefix='/degree')
from backend.models.degree import Degree
from backend.app.forms.degree_form import DegreeForm

@degree_bp.route('/list')
def list_degrees():
    degrees = Degree.query.all()
    return render_template('degree_list.html', degrees=degrees)

@degree_bp.route('/view/<int:degreeID>')
def view_degree(degreeID):
    degree = Degree.query.get_or_404(degreeID)
    return render_template('degree_view.html', degree=degree)

@degree_bp.route('/add', methods=['GET', 'POST'])
def add_degree():
    form = DegreeForm()
    if form.validate_on_submit():
        degree = Degree(**form.data)
        db.session.add(degree)
        db.session.commit()
        flash('Degree added!', 'success')
        return redirect(url_for('degree_bp.list_degrees'))
    return render_template('degree_form.html', form=form)

@degree_bp.route('/edit/<int:degreeID>', methods=['GET', 'POST'])
def edit_degree(degreeID):
    degree = Degree.query.get_or_404(degreeID)
    form = DegreeForm(obj=degree)
    if form.validate_on_submit():
        form.populate_obj(degree)
        db.session.commit()
        flash('Degree updated!', 'success')
        return redirect(url_for('degree_bp.view_degree', degreeID=degree.degreeID))
    return render_template('degree_form.html', form=form)

@degree_bp.route('/delete/<int:degreeID>', methods=['POST'])
def delete_degree(degreeID):
    degree = Degree.query.get_or_404(degreeID)
    db.session.delete(degree)
    db.session.commit()
    flash('Degree deleted.', 'success')
    return redirect(url_for('degree_bp.list_degrees'))
