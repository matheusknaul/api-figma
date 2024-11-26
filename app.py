from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    from main import get_json
    # json = get_json()
    return jsonify(json)


app.run(debug=True)