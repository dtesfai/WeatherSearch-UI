# compose_flask/app.py
import flask
from api.Weather import main

app = flask.Flask(__name__)

@app.route('/api/city/<city>', methods=['GET'])
def get_weather(city):
	return flask.jsonify(main(city))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)