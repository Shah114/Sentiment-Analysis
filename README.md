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


