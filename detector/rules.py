import re
import spacy

# Carregar modelo NLP do spaCy
nlp = spacy.load("pt_core_news_sm")

# Lista expandida de termos ambíguos
AMBIGUOUS_TERMS = {"rápido", "ótimo", "eficiente", "fácil", "melhor", "adequado", "completo"}

def detect_ambiguous_terms(doc):
    """
    Verifica se há termos ambíguos no documento.
    Retorna uma lista de (token.text, token.idx).
    """
    found = []
    for token in doc:
        if token.text.lower() in AMBIGUOUS_TERMS:
            found.append((token.text, token.idx))
    return found

def detect_passive_voice(doc):
    """
    Detecta voz passiva no texto usando regras gramaticais do spaCy.
    Retorna uma lista de sentenças identificadas com voz passiva.
    """
    passive_sentences = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ in {"auxpass", "nsubjpass"}:  # Indica voz passiva
                passive_sentences.append(sent.text)
                break
    return passive_sentences

def detect_vague_pronouns(doc):
    """
    Detecta pronomes vagos no texto, como "isso", "aquilo", "eles".
    """
    vague_pronouns = {"isso", "aquilo", "eles", "estas", "estas", "aquele", "aquela"}
    found = []
    for token in doc:
        if token.lower_ in vague_pronouns:
            found.append((token.text, token.idx))
    return found
