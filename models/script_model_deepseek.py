import os
import requests
from huggingface_hub import HfApi

# Configurações do modelo
REPO_ID = "deepseek-ai/DeepSeek-R1"  # Repositório do modelo
MODEL_PATH = "models/deepseek_r1"    # Pasta onde o modelo será salvo
HF_TOKEN = "SEU_TOKEN_AQUI"          # Substitua pelo seu token de acesso

def get_model_files():
    """
    Obtém a lista de arquivos do repositório do modelo
    """
    api = HfApi(token=HF_TOKEN)
    
    try:
        # Listar todos os arquivos do repositório
        files = api.list_repo_files(repo_id=REPO_ID, repo_type="model")
        return files
    except Exception as e:
        raise RuntimeError(f"Erro ao acessar o repositório: {str(e)}")

def download_model():
    """
    Baixa o modelo DeepSeek-R1
    """
    # Criar pasta models/ se não existir
    if not os.path.exists("models"):
        os.makedirs("models")
        print("📁 Pasta 'models/' criada.")

    # Verificar se o modelo já existe
    if os.path.exists(MODEL_PATH):
        print("✅ Modelo já baixado.")
        return

    try:
        # Obter a lista de arquivos do repositório
        files = get_model_files()
        print(f"🔍 Arquivos encontrados no repositório: {files}")

        # Baixar cada arquivo do repositório
        for file in files:
            file_url = f"https://huggingface.co/{REPO_ID}/resolve/main/{file}"
            file_path = os.path.join(MODEL_PATH, file)
            
            # Criar subpastas, se necessário
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            print(f"⬇️ Baixando {file}...")
            
            # Fazer o download do arquivo com autenticação
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            response = requests.get(file_url, headers=headers, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get("content-length", 0))
            downloaded_size = 0

            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        if total_size > 0:
                            progress = downloaded_size / total_size * 100
                            print(f"Progresso: {progress:.2f}% ({downloaded_size}/{total_size} bytes)", end="\r")
            
            print(f"\n✅ {file} baixado com sucesso!")

        print("\n✅ Todos os arquivos do modelo foram baixados!")

    except Exception as e:
        print(f"❌ Erro durante o download: {str(e)}")
        if os.path.exists(MODEL_PATH):
            os.remove(MODEL_PATH)

if __name__ == "__main__":
    download_model()