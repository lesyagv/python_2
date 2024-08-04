from flask import Blueprint, render_template
from payroll.database import get_db

bp = Blueprint("departments", __name__)

@bp.route("/departments/index")
def index():
    db = get_db()
    departments = db.execute("SELECT id, department_name FROM department").fetchall()

    return render_template('departments/index.html', departments = departments)

@bp.route("/departments/create")
def create():
    db = get_db()
    departments = db.execute('SELECT id, department_name FROM department').fetchall()
    return render_template("departments/create.html", departments=departments)