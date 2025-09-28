from flask import Flask, jsonify, make_response, request, render_template, url_for
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_function():
    # Get the query parameter "textToAnalyze"
    text_to_analyze = request.args.get("textToAnalyze", "")
    # Return it back as plain text
    text_analysed = emotion_detector(text_to_analyze) 
    return "For the given statement, the system response is 'anger': " + str(text_analysed["anger"]) + ", 'disgust': " + str(text_analysed["disgust"]) + ", 'fear': " + str(text_analysed["fear"]) + ", 'joy': " + str(text_analysed["joy"]) + " and 'sadness': " + str(text_analysed["sadness"]) + ". The dominant emotion is " + str(text_analysed["dominant_emotion"]) + "."

if __name__ == "__main__":
    app.run(debug=True)