from flask import Blueprint, render_template
from payroll.database import get_db

bp = Blueprint("roles", __name__)

@bp.route("/roles/index")
def index():
    db = get_db()
    roles = db.execute("SELECT id, role_name FROM roles").fetchall()
    return render_template('roles/index.html', roles = roles)

@bp.route("/roles/create")
def create():
    db = get_db()
    roles = db.execute("SELECT id, role_name FROM roles").fetchall()
    return render_template('roles/create.html', roles = roles)