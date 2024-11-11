from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Initialize the analyzer and anonymizer
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Sample text to analyze
text = "My phone number is 123-456-7890."

# Analyze the text
results = analyzer.analyze(text=text, language='en')

# Print the results of the analysis
for result in results:
    print(f"Entity: {result.entity_type}, Score: {result.score}, Position: {result.start}-{result.end}")

# Anonymize the text (optional)
anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

print(f"Anonymized Text: {anonymized_text.text}")
