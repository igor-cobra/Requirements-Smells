import os
import requests

MODEL_URL = "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf"
MODEL_PATH = "models/llama-2-7b.Q4_K_M.gguf"

def download_model():
    """
    Verifica se o modelo já está baixado. Se não estiver, cria a pasta e faz o download.
    """
    # Criar pasta models/ se não existir
    if not os.path.exists("models"):
        os.makedirs("models")
        print("Pasta 'models/' criada.")

    # Verificar se o modelo já existe
    if os.path.exists(MODEL_PATH):
        print("Modelo já baixado.")
        return

    print(f"Baixando modelo de {MODEL_URL}...")

    # Fazer o download do modelo
    response = requests.get(MODEL_URL, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with open(MODEL_PATH, "wb") as model_file:
        downloaded_size = 0
        for chunk in response.iter_content(1024):
            if chunk:
                model_file.write(chunk)
                downloaded_size += len(chunk)
                print(f"Baixando... {downloaded_size / total_size * 100:.2f}%", end="\r")

    print("\nDownload concluído!")

if __name__ == "__main__":
    download_model()
