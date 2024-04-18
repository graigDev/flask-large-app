from flask import Blueprint

bp = Blueprint('auth', __name__)

from src.features.auth import routes
