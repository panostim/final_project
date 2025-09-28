from flask import Flask, jsonify, make_response, request, render_template, url_for
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector/", methods=["GET"])
def emotionDetectionfunction():
    if request.method == 'GET':
        x="Example response"
        # Redirect to the transactions list page after adding the new transaction
        return x

@app.route("/emotionDetector/", methods=["POST"])
def submitText():
    if request.method == 'POST':
        #x="Example response"
        text = request.form.get("textToAnalyze")
        # Redirect to the transactions list page after adding the new transaction
        return text


if __name__ == "__main__":
    app.run(debug=True)