from src.search.search import search_context
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    answers = search_context(question)
    return jsonify({'answers': answers})

if __name__ == "__main__":
    app.run(debug=True)