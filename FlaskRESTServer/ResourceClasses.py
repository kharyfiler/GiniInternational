from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///GiniInternationalDataDB.db')  # original value is 'chinook.db'
app = Flask(__name__)
api = Api(app)


class ApiRoot(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Country from giniTable")
        result = {"data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Country(Resource):
    def get(self, country):
        conn = db_connect.connect()
        country_string = "LOCATION" if len(country) == 3 else "Country"
        query = conn.execute("select Country, MEASURE_ABBR, Value from giniTable where " + country_string + " = ?", country)
        result = {"data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class CountryMeasure(Resource):
    def get(self, country, measure):
        conn = db_connect.connect()
        country_string = "LOCATION" if len(country) == 3 else "Country"
        query = conn.execute("select Country, Value from giniTable where " + country_string + " = ? and MEASURE_ABBR = ?", country, measure)
        # query.keys() is a list of values. In this case, ['Country', 'Value']
        # tuple(query.keys()) turns the list into a tuple. In this case, from ['Country', 'Value'] to ('Country', 'Value')
        # the query.cursor contains an iterable list of objects(tuples?)
        # "i" is a tuple. A tuple is a finite ordered list?
        # the cursor begins before the first row and is moved to the next row after each row is read. The cursor returns false
        # when it is positioned after the last row
        result = {"data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(ApiRoot, '/api')
api.add_resource(Country, '/api/<country>')
api.add_resource(CountryMeasure, '/api/<country>/<measure>')

if __name__ == '__main__':
    app.run(port='5002')