# Detecção de Requirements Smells e Code Review com IA
 Um projeto para análise de requisitos de software, criado para um projeto para a disciplina de Resolução de Problemas da UTFPR-DV
 
Este projeto implementa um sistema de detecção de *requirements smells* e revisão de código com IA, utilizando modelos de NLP e aprendizado de máquina para analisar requisitos e trechos de código, fornecendo feedback estruturado.

## Tecnologias Utilizadas
- **Python**
- **Flask** (para interface web)
- **spaCy** (para processamento de linguagem natural)
- **Llama** (para análise com IA generativa)
- **CodeBERT** (para detecção de *code smells*)
- **Pandas** (para geração de relatórios)

## Estrutura do Projeto
```
/
├── app.py                 # Aplicativo Flask
├── detector/
│   ├── ai_code_reviewer.py  # Revisão de requisitos com IA
│   ├── ml_classifier.py     # Classificação de problemas de código
│   ├── nlp_processor.py     # Processamento de texto
│   ├── report.py            # Geração de relatórios
│   ├── rules.py             # Regras para identificação de problemas
├── templates/
│   ├── index.html           # Interface web
├── README.md
```

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Baixe os modelos necessários:
   ```sh
   python -m spacy download en_core_web_sm
   python -m spacy download pt_core_news_sm
   ```
4. Execute o aplicativo:
   ```sh
   python app.py
   ```

## Uso
1. Acesse `http://127.0.0.1:5000/` no navegador.
2. Insira um requisito ou trecho de código na caixa de entrada.
3. Clique no botão "Analisar".
4. O sistema exibirá:
   - Relatório de *requirements smells*.
   - Feedback gerado por IA.
   - Identificação de *code smells*.

## Contribuição
Sinta-se à vontade para enviar *pull requests* ou relatar problemas na [seção de issues](https://github.com/seu-usuario/seu-repositorio/issues).

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

