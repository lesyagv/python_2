from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")
    #return "Home page."

@bp.route("/about")
def about():
    return render_template("pages/about.html")
    #return "About page."

@bp.route("/auth")
def auth():
    return render_template("pages/auth.html")

@bp.route("/login")
def login():
    return render_template("pages/login.html")
