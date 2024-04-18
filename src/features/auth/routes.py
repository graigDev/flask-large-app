from flask import render_template
from src.features.auth import bp


@bp.route('/login')
def login():
    return render_template('views/auth/login.html')


@bp.route('/register')
def register():
    return render_template('views/auth/register.html')


@bp.route('/forgot_password')
def forgot_password():
    return render_template('views/auth/forgot_password.html')


@bp.route('/reset_password')
def reset_password():
    return render_template('views/auth/reset_password.html')