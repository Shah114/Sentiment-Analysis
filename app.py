# Importing Modules
from flask import Flask, render_template, request
from transformers import pipeline

# Creating Flask app
app = Flask(__name__, template_folder="C:/Projects/ComprehensivePipeline/templates")

# Load only the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Function
@app.route('/', methods=['GET', 'POST'])
def index():
    sent = None
    user_input = None # Define user_input variable
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        if user_input:
            sent = sentiment_pipeline(user_input)

    return render_template('index.html', sent=sent, user_input=user_input)

# Main part
if __name__ == '__main__':
    app.run(debug=True)