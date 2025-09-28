"""
Flask web application for performing emotion detection on text submitted by the user.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

@app.route("/")
def home():
    """
    URL for handling the html template rendering
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    URL for handling the user submitted data and the response
    """
    # Get the input
    text_to_analyze = request.args.get("textToAnalyze", "")
    # Return it back as plain text
    text_analysed = emotion_detector(text_to_analyze)
    # Return the result
    return (
    f"For the given statement, the system response is "
    f"'anger': {text_analysed['anger']}, "
    f"'disgust': {text_analysed['disgust']}, "
    f"'fear': {text_analysed['fear']}, "
    f"'joy': {text_analysed['joy']} and "
    f"'sadness': {text_analysed['sadness']}. "
    f"The dominant emotion is {text_analysed['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(debug=True)
