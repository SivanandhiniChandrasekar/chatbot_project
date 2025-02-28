from flask import Flask, render_template, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
import os

# Initialize Flask app
app = Flask(__name__)

# Load documentation files
DOCS_DIR = "docs"
docs = {}
print(word_tokenize("Hello, how are you?"))

doc_files = ["segment_docs.txt", "mparticle_docs.txt", "lytics_docs.txt", "zeotap_docs.txt"]
for file in doc_files:
    file_path = os.path.join(DOCS_DIR, file)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            docs[file.split("_")[0]] = f.read()

# Function to process user query and match it with docs
def search_docs(query):
    try:
        print(f"Raw Query: {query}")  # Debugging step
        if not query.strip():
            return "Error: Empty query received."
        
        query_tokens = word_tokenize(query.lower())
        print(f"Query Tokens: {query_tokens}")  # Debugging step
        
        if not query_tokens:
            return "Error: Tokenization failed, check input format."

        relevant_texts = []
        for platform, doc in docs.items():
            found_tokens = [token for token in query_tokens if token in doc.lower()]
            print(f"Checking {platform} docs: Found Tokens - {found_tokens}")  # Debugging step

            if found_tokens:
                # Extract the most relevant section (first 300 chars as an example)
                extracted_info = doc[:300] + "..." if len(doc) > 300 else doc
                
                # Format the response in a structured way
                response = f"""
                📌 **Relevant Information from {platform.capitalize()} Docs:**
                
                {extracted_info}
                """
                relevant_texts.append(response)
        if relevant_texts:
            return "\n".join(relevant_texts)
        else:
            return "❌ *Sorry, no relevant information found. Try rephrasing your query!*"
    except Exception as e:
        return f"Error processing query: {str(e)}"


# Route to render the chatbot UI
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user query
@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form.get('user_input', '').strip()
    if not user_input:
        return jsonify({"reply": "⚠️ Please enter a valid question!"})

    print(f"🔹 Received Input: {user_input}")  # Debugging log

    response = search_docs(user_input)
    return response
  

if __name__ == '__main__':
    app.run(debug=True)
