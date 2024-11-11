from flask import Flask, request, jsonify
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

app = Flask(__name__)

@app.route('/analyze_and_anonymize', methods=['POST'])
def analyze_and_anonymize():
    data = request.json.get('text', '')
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()

    # Analyze the text for sensitive information
    results = analyzer.analyze(text=data, language='en')

    # Anonymize the text based on the analysis
    anonymized_text = anonymizer.anonymize(text=data, analyzer_results=results)

    return jsonify({'anonymized_text': anonymized_text.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
