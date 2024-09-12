# Sentiment-Analysis
This project demonstrates a Sentiment Analysis model using the transformers library's pipeline. The model classifies text into positive, negative, or neutral sentiments. The project is powered by a Flask API for backend functionality and an HTML front end. <br/>
<br/>

## Features
* Sentiment Analysis: Utilizes Hugging Face's transformers pipeline to analyze and classify sentiments from text input.
* Flask API: Provides a simple API to serve the sentiment analysis model.
* Front-end: Contains an HTML form for user input and displays the sentiment prediction result. <br/>
<br/>

## Project Structure
```graphql
.
├── app.py                 # Main Flask application
├── templates
│   └── index.html         # Front-end HTML file
├── requirements.txt       # Dependencies required for the project
└── README.md              # This README file
```
<br/>

## Setup Instructions
1. Clone the Repository
   
   ```bash
   git clone https://github.com/Shah114/Sentiment-Analysis.git
   cd sentiment-analysis-flask
   ```
2. Create a Virtual Environment (Optional)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask Application
   ```bash
   python app.py
   ```
<br/>

## Dependencies
* Python 3.7+
* Flask
* transformers (for Hugging Face sentiment analysis model)
* Any other necessary packages listed in requirements.txt <br/>
<br/>

## How it Works
The sentiment analysis is performed using Hugging Face's pipeline from the transformers library. The input text is classified into one of three categories: positive, negative, or neutral. <br/>
* Input: The user provides text input through the front-end form in index.html.
* Prediction: The text is sent to the Flask API, which processes it using the sentiment analysis pipeline.
* Output: The predicted sentiment is displayed on the webpage. <br/>
<br/>

## Future Enhancements
* Add more complex sentiment classification models.
* Enhance front-end UI with additional features and animations.
* Improve error handling for invalid inputs. <br/>
<br/>

## Contrubuting
Contributions are welcome! Feel free to open an issue or submit a pull request.



