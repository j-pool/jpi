__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

from flask import Blueprint
from jpi.json_utils import jsonify
from jpi.games.mocks import MOCK_GAMES

games = Blueprint('games', __name__, url_prefix='/games')

@games.route('/')
def get_games():
	return jsonify(games=MOCK_GAMES)

@games.route('/<int:year>')
def get_games_by_year(year):
	return jsonify(games=MOCK_GAMES[2012-year])

@games.route('/<int:year>/<int:week>')
def get_games_by_week(year, week):
	return jsonify(games=MOCK_GAMES[2012-year][week-1])