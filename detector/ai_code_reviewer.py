from llama_cpp import Llama
import logging

# Configurar logging para depuração
logging.basicConfig(level=logging.DEBUG)

# Carregar o modelo Llama
llm = Llama(model_path="models/llama-2-7b.Q4_K_M.gguf")

def analyze_text(text):
    """
    Envia o texto para o Llama e recebe feedback detalhado sobre ambiguidades, clareza e estrutura.
    """
    prompt = f"""
    Analise o seguinte requisito e forneça um feedback estruturado. Responda APENAS com a análise e nada mais.

    REQUISITO:
    "{text}"

    **RESPOSTA ESPERADA (Exemplo de formato que você deve seguir, sem incluir esta instrução na resposta final):**
    - **Clareza:** [Diga se o requisito é claro e sugira melhorias]
    - **Ambiguidade:** [Liste os termos ambíguos e sugira correções]
    - **Estrutura Gramatical:** [Identifique erros e sugira melhorias]
    - **Voz Ativa ou Passiva:** [Se estiver em voz passiva, reescreva o requisito na voz ativa]

    **IMPORTANTE:**
    - NÃO copie o enunciado.
    - NÃO inclua introduções como "Aqui está sua resposta".
    - NÃO repita as perguntas, apenas forneça a resposta estruturada.
    """

    output = llm(prompt, max_tokens=100000)

    # Verificar se a IA realmente respondeu corretamente
    resposta_completa = output["choices"][0]["text"].strip() if "choices" in output else "Erro na resposta da IA."

    # Se a resposta ainda parecer um reflexo do prompt, logamos para depuração
    if resposta_completa.lower().startswith("analise o seguinte requisito") or "REQUISITO" in resposta_completa:
        logging.warning("A IA pode estar apenas repetindo o prompt. Saída bruta:")
        logging.warning(resposta_completa)

    logging.debug(f"Saída bruta da IA para depuração: {resposta_completa}")
    
    return resposta_completa
