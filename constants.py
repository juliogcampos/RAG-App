"""Módulo responsável por armazenar constantes da aplicação."""

from typing import Final

# Diretório da aplicação
APP_PATH: Final[str] = "app.py"

# Diretório do banco de dados vetorial do Chroma
CHROMA_PATH: Final[str] = "db/chroma"

# Diretório onde estão armazenados os arquivos carregados na aplicação
DATA_PATH: Final[str] = "data"

# Arquivo CSS da aplicação
CSS_PATH: Final[str] = "src/views/css/style.css"

# Diretório de arquivos de testes da aplicação
FILE_TESTS_PATH: Final[str] = "test/file_tests"

### ---------- Ollama ---------- ###

# Endpoint da API
OLLAMA_BASE_ENDPOINT: Final[str] = 'http://localhost:11434'

# Endpoint dos modelos baixados pelo Ollama
OLLAMA_MODELS_ENDPOINT: Final[str] = f'{OLLAMA_BASE_ENDPOINT}/api/tags'


### ---------- Streamlit ---------- ###

# chave de estado de sessão que armazena nome da llm selecionada pelo usuário
LLM_NAME: Final[str] = "llm_name"

# chave de estado de sessão que armazena arquivos carregados pelo usuário
UPLOADED_FILES: Final[str] = "uploaded_files"

# chave de estado de sessão que armazena a pergunta do usuário
QUESTION: Final[str] = "question"

# chave de estado de sessão que armazena dados de perguntas e respostas do usuário
QUESTIONS: Final[str] = "questions_and_answers"
