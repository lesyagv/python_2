from flask import Blueprint, render_template
from payroll.database import get_db

bp = Blueprint("roles", __name__)

@bp.route("/roles/index")
def index():
    db = get_db()
    roles = db.execute("SELECT id, role_name FROM roles").fetchall()
    return render_template('roles/index.html', roles = roles)

@bp.route("/roles/create", methods=('GET', 'POST'))
@login_required
def create():
    db = get_db()
    roles = db.execute("SELECT id, role_name FROM roles").fetchall()
    return render_template('roles/create.html', roles = roles)

@bp.route('/roles/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    db = get_db()
    roles = db.execute("SELECT id, role_name FROM roles").fetchall()
    if request.method == "POST":
        role_id = int(request.form['role_id'])

        error = None

        if not role_name:
            error = "role is required!"

        if error is not None:
            flash(error, category="error")
        else:
            db = get_db()

            db.execute(
                "UPDATE role SET role_id = ? WHERE id=?",
                (role_id, id)
            )

            db.commit()
        current_app.logger.info(f"role {role_name} was updated")
        flash(f"role {role_name} was updated", category="success")
    return render_template('roles/index.html', roles=roles)

@bp.route('/roles/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    db = get_db()
    db.execute('DELETE FROM role WHERE id=?', (id,))
    db.commit()
    return redirect(url_for("role.index"))