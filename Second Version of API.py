# Need a way to deploy my regression model into production
# Best options from reddit.com/r/datascience questioning:
#  -FLASK
#  -Domino Data Lab
# Info:
# http://flask.pocoo.org/snippets/96/
#  -No need for Server with Wordpress info https://managewp.com/wordpress-custom-code

import pandas as pd
from flask import Flask, render_template, jsonify, make_response, request
from flask_restplus import Api
from flask_restplus import fields
from sklearn.externals import joblib
import requests


app = Flask(__name__)


#api = Api(
#    app,
#    version='1.0',
#    description = 'A better way to prediction your property')
#ns = api.namespace('property_value',
#     description = 'Insight to true value')


#parser=api.parser()

#parser.add_agrument('Rent Roll/expenses',
#    type=float,
#    required=True,
#    help='This will help guide your true value in terms of CAP Rate',
#    location='form')

#parser.add_agrument('Number of Units',
#    type=int,
#    required=True,
#    help='Number of Units in the property.',
#    location='form')

#parser.add_agrument('Square Footage',
#    type=int,
#    required=True,
#    help='How many square feet make up your building?',
#    location='form')

#parser.add_agrument('Year Built',
#    type=int,
#    required=True,
#    help='What year was your property built?',
#    location='form')

#parser.add_agrument('Zip Code',
#    type=str,
#    required=True,
#    help='What is the zip code of the location of your building?',

#resource_fields= api.model('Resource', {'results': fields.String,})




from flask.ext.restplus import Resource
@ns.route('/')
class Propertyvalue(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def post(self):
        args = parser.parser_args()
        results = self.get_results(args)

    #    return results,201??????

    def get_results(self,agrs):
        cap = agrs["Rent Roll/expenses"]
        units = agrs["Number of Units"]
        sqft = agrs["Square Footage"]
        year = agrs["Year Built"]
        zipper = agrs["Zip Code"]

        from pandas import DataFrame
        a= DataFrame([[
        cap,
        units,
        sqft,
        year,
        zipper
    ]])

        value = results.predict(a)

        return value


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':

    app.run(debug=True, host='localhost')
