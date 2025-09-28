from flask import Flask, jsonify, make_response, request
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

@app.route("/", methods=['GET'])
def emotionDetector():
    # Function that handles requests to the root URL
    # Return a plain text response
    return emotion_detector('I feel disgusted just hearing about this')


if __name__ == "__main__":
    app.run(debug=True)