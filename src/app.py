from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = True

# Create some test data for our catalog in the form of a list of dictionaries.
weather = [
   {"date":"2020-06-29T13:14:34.8698384-04:00","temperatureC":-5,"temperatureF":24,"summary":"Balmy"}
   ,{"date":"2020-06-30T13:14:34.875111-04:00","temperatureC":52,"temperatureF":125,"summary":"Sweltering"}
   ,{"date":"2020-07-01T13:14:34.8751169-04:00","temperatureC":47,"temperatureF":116,"summary":"Hot"}
   ,{"date":"2020-07-02T13:14:34.8751176-04:00","temperatureC":42,"temperatureF":107,"summary":"Hot"}
   ,{"date":"2020-07-03T13:14:34.875118-04:00","temperatureC":-4,"temperatureF":25,"summary":"Balmy"}
   
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sample Weather API</h1>
<p>A prototype API for weather of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/weather', methods=['GET'])
def api_all():
    return jsonify(weather)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')