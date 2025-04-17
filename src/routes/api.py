from flask import Flask, request, jsonify
from search.search import search_context

app = Flask(__name__)

@app.route('/api/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    answer = search_context(question)
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)