__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions

def json_app(app):
	def jsonify_unhandled_exceptions(e):
		response = jsonify(message=str(e))
		response.status_code = getattr(e, 'code', 500)
		return response

	for status_code in default_exceptions.keys():
		app.error_handler_spec[None][status_code] = jsonify_unhandled_exceptions
	return app

app = json_app(Flask(__name__))

from jpi.scores.scores import scores
from jpi.spreads.spreads import spreads

app.register_blueprint(scores)
app.register_blueprint(spreads)