import pandas as pd
from bigframes.dataframe import DataFrame
from typing import Any, Callable, Dict, List, Union
from presidio_structured import StructuredEngine, PandasAnalysisBuilder
from presidio_anonymizer.entities import OperatorConfig
bf.close_session()
bf.options.bigquery.location = "us" #this variable is set based on the dataset you chose to query
bf.options.bigquery.project = "perseus-curation-stg-1274" #this variable is set based on the dataset you chose to query
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_anonymizer import AnonymizerEngine

registry = RecognizerRegistry()
registry.load_predefined_recognizers(languages=['en'])

# Set up analyzer with our updated recognizer registry
analyzer = AnalyzerEngine(registry=registry)
anonymizer = AnonymizerEngine()
def hash_pii_using_presidio(text, entities=None):

    if entities is None:
        entities = ['IBAN_CODE', "EMAIL_ADDRESS", "PHONE_NUMBER", "CREDIT_CARD", 'IP_ADDRESS', 'PERSON']
    else:
        entities = entities.split(',')

    # If the text contains an email address, replace only %40 with @
    if 'EMAIL_ADDRESS' in entities:
        text = text.replace('%40', '@')  # Replace only %40 with @

    # Call analyzer to get results
    analyzer_results = analyzer.analyze(text=text,
                                        entities=entities,
                                        language='en')

    # Analyzer results are passed to the AnonymizerEngine for anonymization
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=analyzer_results)

    return anonymized_text.text
