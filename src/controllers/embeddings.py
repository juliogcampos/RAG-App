"""Módulo responsável pela utilização de modelos de incorporação."""

from langchain_core.embeddings import Embeddings
from langchain_community.embeddings import GPT4AllEmbeddings


def get_default_text_embedding() -> Embeddings:
    """Função que define o modelo de incorporação de texto padrão a ser utilizado pela aplicação.

    Returns:
        Embeddings: modelo de incorporação de texto.
    """
    return gpt4all()


def gpt4all() -> Embeddings:
    """Função que retorna modelo de incorporação de texto do GPT4All, da Nomic.

    Docs: 
        https://docs.gpt4all.io/gpt4all_python_embedding.html

    Returns:
        Embeddings: Modelo de incorporação de texto do GPT4All.
    """
    # definir modelo que possui comprimento de contexto de 2048 tokens.
    embeddings = GPT4AllEmbeddings(model_name="nomic-embed-text-v1.5.f16.gguf")
    return embeddings
