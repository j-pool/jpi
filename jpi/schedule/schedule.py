__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com'

from flask import Blueprint, jsonify

schedule = Blueprint('schedule', __name__, url_prefix='/api/schedule')