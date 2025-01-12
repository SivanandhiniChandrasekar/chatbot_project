from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize
import os

# Initialize Flask app
app = Flask(__name__)

# Load documentation files
docs = {
    'segment': open('docs/segment_docs.txt').read(),
    'mparticle': open('docs/mparticle_docs.txt').read(),
    'lytics': open('docs/lytics_docs.txt').read(),
    'zeotap': open('docs/zeotap_docs.txt').read(),
}

# Function to process user query and match it with docs
def search_docs(query):
    # Tokenize query
    query_tokens = word_tokenize(query.lower())
    
    # Simple keyword search for the query
    response = ''
    for platform, doc in docs.items():
        if any(keyword in doc.lower() for keyword in query_tokens):
            response += f"Found relevant information in {platform} docs.\n"
    
    if not response:
        response = "Sorry, I couldn't find relevant information."
    return response

# Route to render the chatbot UI
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user query
@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = search_docs(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
