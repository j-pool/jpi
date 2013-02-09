__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com'

from flask import Blueprint
from jpi.json_utils import jsonify
from jpi.schedule.constants import MOCK_SCHEDULE

schedule = Blueprint('schedule', __name__, url_prefix='/schedule')

@schedule.route('/')
def get_schedule():
	return jsonify(schedule=MOCK_SCHEDULE)

@schedule.route('/<int:year>')
def get_schedule_by_year(year):
	return jsonify(schedule=MOCK_SCHEDULE[2012-year])

@schedule.route('/<int:year>/<int:week>')
def get_schedule_by_week(year, week):
	return jsonify(schedule=MOCK_SCHEDULE[2012-year][week-1])