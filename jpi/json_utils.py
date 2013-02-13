__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

import json
import datetime
from flask import Response

class JPLEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return super(JPLEncoder, self).default(obj)

def jsonify(*args, **kwargs):
    payload = json.dumps(dict(*args, **kwargs), cls=JPLEncoder)
    return Response(payload, mimetype='application/json')