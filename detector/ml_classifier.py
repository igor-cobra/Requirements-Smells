from transformers import pipeline

# Usa um modelo de NLP para detectar problemas no código
review_pipeline = pipeline("text-classification", model="microsoft/codebert-base")

def detect_code_smells(code_snippet):
    # Classifica trechos de código como "code smell" ou "clean".
    prediction = review_pipeline(code_snippet)
    return prediction
