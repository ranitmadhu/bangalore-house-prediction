import flask
import requests
from flask import request,jsonify
import util
app = flask.Flask(__name__)
@app.route('/ get_location_name')

def get_location_name():
    response = jsonify({
        'locations':util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.json['total_sqft'])
    location_name=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    resource=jsonify({
        "estimated_price":util.get_estimated_price(total_sqft,location_name,bhk,bath)
    })
    resource.headers.add('Access-Control-Allow-Origin', '*')
    return resource


if __name__ == '__main__':
    app.run(debug=True)