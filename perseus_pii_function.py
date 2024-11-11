from bigframes.dataframe import DataFrame
from typing import Any, Callable, Dict, List, Union
bf.close_session()
bf.options.bigquery.location = "us" #this variable is set based on the dataset you chose to query
bf.options.bigquery.project = "perseus-curation-stg-1274" #this variable is set based on the dataset you chose to query
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Set up analyzer with our updated recognizer registry
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

#@bf.remote_function([str, str], str, packages=["presidio_anonymizer", "presidio_analyzer"], dataset='test', name='hash_pii_venkat', reuse=True, bigquery_connection='perseus-curation-stg-1274.us.perseus-curation-stg-1274_cloud_resource_connection', cloud_function_memory_mib='3000', max_batching_rows=1000)
def hash_pii_using_presidio('venk.113@gmail.com', entities='EMAIL_ADDRESS'):

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
