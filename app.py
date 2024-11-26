from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    from main import get_json
    json = get_json("IQHFsrTcXpJsMY2M6aopyY", "figd_JnR3V2SivkMrY7nQNQuGinxkYx2H5pfivFR0Pp-H")
    return jsonify(json)


app.run(debug=True)