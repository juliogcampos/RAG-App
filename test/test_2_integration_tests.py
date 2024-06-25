"""Módulo de testes de integração da aplicação desenvolvidos com Pytest."""

from typing import List
from io import BytesIO

from src.controllers.files import (
    delete_uploaded_files,
    get_list_of_uploaded_files,
    index_files)
from src.controllers.vector_db import clear_chroma_db, get_docs_of_chroma


def test_index_files():
    """Função que testa a indexação, divisão e armazenamento de arquivos carregados na aplicação."""

    # limpar banco de dados vetorial
    clear_chroma_db()

    # Criar um arquivo de texto de teste
    text_content = "Olá mundo!"
    text_file = BytesIO(text_content.encode("utf-8"))
    text_file.name = "txt_test_file.txt"
    text_file.type = "text/plain"

    # Indexar arquivos de teste
    index_files([text_file])

    # Indexar os mesmos arquivos de teste novamente
    index_files([text_file])

    # Obter lista de arquivos do banco de dados vetorial
    docs: List = get_docs_of_chroma()

    assert len(docs) > 0, "A lista de documentos carregados deve ser maior que zero"


def test_delete_uploaded_files():
    """Função que testa a remoção de arquivos carregados."""

    # Deletar arquivo de teste
    delete_uploaded_files()

    # Obter lista de arquivos carregados pelo usuário
    files: List = get_list_of_uploaded_files()

    assert files == [], "A lista de arquivos carregados pelo usuário deve ser vazia"
