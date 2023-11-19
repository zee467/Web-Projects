from flask import Blueprint, render_template

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register")
def register():
    # Registration logic...
    return render_template("registration.html")

@auth_bp.route("/login")
def login():
    # Login logic...
    return render_template("login.html")