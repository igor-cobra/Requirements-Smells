# detector/report.py
import pandas as pd

def generate_report(requisito: str, ambiguous_terms, passive_sentences, vague_pronouns):
    """
    Gera um relatório básico em formato de dicionário e também como uma tabela (usando pandas).
    """
    report = {
        "Requisito": requisito,
        "Termos Ambíguos": ambiguous_terms,
        "Sentenças em Voz Passiva": passive_sentences,
        "Pronomes Vagos": vague_pronouns
    }
    df = pd.DataFrame.from_dict(report, orient="index", columns=["Detalhes"])
    return report, df.to_html()

if __name__ == "__main__":
    # Exemplo de uso
    sample_text = "The system should be fast and it must be user-friendly. It was developed by the team."
    from detector.nlp_processor import process_text
    from detector.rules import detect_ambiguous_terms, detect_passive_voice, detect_vague_pronouns

    doc = process_text(sample_text)
    amb = detect_ambiguous_terms(doc)
    passive = detect_passive_voice(doc)
    pronouns = detect_vague_pronouns(doc)
    report_dict, report_html = generate_report(sample_text, amb, passive, pronouns)
    print(report_dict)
    # Você pode salvar report_html em um arquivo ou integrá-lo na interface web.
