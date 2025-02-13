from flask import Flask, render_template, request, redirect, url_for
from detector.nlp_processor import process_text
from detector.rules import detect_ambiguous_terms, detect_passive_voice, detect_vague_pronouns
from detector.report import generate_report
from detector.ai_code_reviewer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        requisito = request.form.get("requisito")
        if not requisito:
            return redirect(url_for("index"))
        
        doc = process_text(requisito)
        ambiguous_terms = detect_ambiguous_terms(doc)
        passive_sentences = detect_passive_voice(doc)
        vague_pronouns = detect_vague_pronouns(doc)
        
        try:
            ia_feedback = analyze_text(requisito)  # Agora chamamos a IA corretamente
        except Exception as e:
            ia_feedback = f"Erro ao processar análise da IA: {str(e)}"
        
        report_dict, report_html = generate_report(requisito, ambiguous_terms, passive_sentences, vague_pronouns)
        
        return render_template("index.html", report=report_html, requisito=requisito, ia_feedback=ia_feedback)
    
    return render_template("index.html", report=None, ia_feedback=None)



if __name__ == "__main__":
    app.run(debug=True)
