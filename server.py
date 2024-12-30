"""Emotion Detector Flask Application

This Flask application takes text input from a user, performs emotion detection using 
an external API,and returns the predicted emotions and dominant emotion.
"""

from flask import Flask, render_template, request

# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """
    This function receives the text from the HTML interface and runs emotion detection over
    it using emotion_detection() function.
    The output returned shows the emotions scores and dominant emotion for the provided text.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return {"error_message": "Input parameter missing"}, 422

    response = emotion_detector(text_to_analyze=text_to_analyze)
    keys = list(response.keys())

    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    # Return a formatted string with the emotion scores
    return (f"For the given statement, the system response is:\n"
            f"{keys[0]}: {response['anger']}, {keys[1]}: {response['disgust']}, \n"
            f"{keys[2]}: {response['fear']}, {keys[3]}: {response['joy']}, \n"
            f"{keys[4]}: {response['sadness']}. The dominant emotion is \n"
            f"{response['dominant_emotion']}.")


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page over the Flask channel.
    """
    return render_template('index.html')


app.run(host="0.0.0.0", port=5000)
