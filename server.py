"""Flask server for emotion detection application."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home_page():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """Detect the emotions in the provided text and return the results."""
    text = request.args.get("textToAnalyze", "")
    result = emotion_detector(text)
    print(result)
    if result['dominant_emotion'] is None:
        response = jsonify({"response": "Invalid text! Please try again!"})
        response.status_code = 400
    else:
        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )

    return response

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
