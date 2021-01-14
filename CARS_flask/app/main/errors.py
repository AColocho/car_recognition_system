from . import main
from flask import render_template

@main.app_errorhandler(404)
def PageNotFound(e):
    return render_template('error.html',error = 404)

@main.app_errorhandler(500)
def ServerError(e):
    return render_template('error.html',error = 500)