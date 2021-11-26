from flask import Flask, jsonify, request
import joblib
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@cross_origin(origin='*')
def index():
    
    
    data = request.get_json()
    
    # check if gender and age are there in data dictionary
    if not data['gender'] or not data['age']:
        return jsonify({
            "message": "All fields are compulsory"
        })

    if data['gender'].lower() == 'male':
        gender = 1
    elif data['gender'].lower() == 'female': 
        gender = 0
    else:
        return jsonify({
            'message': 'Cannot detect this gender'
        })

    if data['age'] < 2:
        return jsonify({
            'message': 'Do you even listen to songs'
        })

    # load the model
    model = joblib.load('music-recommender.joblib')
    prediction = model.predict([[ data['age'], gender ]])
    
    return jsonify({
        'message': 'Successfully found a genre for you...',
        'genre': prediction[0]
    })

    if request.method == 'GET':
        return jsonify({
            'message': 'Hello World!'
        })

app.run()