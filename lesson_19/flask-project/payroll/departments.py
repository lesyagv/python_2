from flask import Blueprint, render_template, request, flash, current_app, redirect, url_for
from payroll.database import get_db
from werkzeug.exceptions import abort

bp = Blueprint("departments", __name__)

@bp.route("/departments/index")
def index():
    db = get_db()
    departments = db.execute("SELECT id, department_name FROM department").fetchall()

    return render_template('departments/index.html', departments = departments)

@bp.route("/departments/create", methods=('GET', 'POST'))
@login_required
def create():
    db = get_db()
    departments = db.execute('SELECT id, department_name FROM department').fetchall()
    return render_template("departments/create.html", departments=departments)

@bp.route('/departments/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    db = get_db()
    departments = db.execute('SELECT id, department_name FROM department').fetchall()
    if request.method == "POST":
        department_id = int(request.form['department_id'])
        error = None

        if not department_name:
            error = "department is required!"

        if error is not None:
            flash(error, category="error")
        else:
            db = get_db()

            db.execute(
                "UPDATE department SET department_id = ? WHERE id=?",
                (department_id, id)
            )

            db.commit()
        current_app.logger.info(f"department {department_name} was updated")
        flash(f"department {department_name} was updated", category="success")
    return render_template("departments/index.html", departments=departments)

@bp.route('/departments/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    db = get_db()
    db.execute('DELETE FROM department WHERE id=?', (id,))
    db.commit()
    return redirect(url_for("departments.index"))



