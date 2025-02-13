# detector/nlp_processor.py
import spacy

# Carregue o modelo do spaCy (modelo pequeno; para produção, considere um modelo maior)
nlp = spacy.load("en_core_web_sm")

def process_text(text: str):
    """
    Processa o texto do requisito e retorna o objeto Doc do spaCy.
    """
    doc = nlp(text)
    return doc

def extract_sentences(doc):
    """
    Retorna uma lista de sentenças do objeto Doc.
    """
    return list(doc.sents)

def get_pos_tags(doc):
    """
    Retorna uma lista de tuplas (token.text, token.pos_, token.tag_) para cada token.
    """
    return [(token.text, token.pos_, token.tag_) for token in doc]