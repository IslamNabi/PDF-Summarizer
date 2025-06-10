from flask import Flask, request, jsonify
from summarizer import extract_text, summarize

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def handle_summarize():
    if 'file' not in request.files:
        return jsonify({"error": "No PDF uploaded"}), 400
    
    file = request.files['file']
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Invalid file type"}), 400
    
    try:
        text = extract_text(file)
        summary = summarize(text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)