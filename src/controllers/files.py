"""Módulo que armazena funções de gerenciamento de arquivos da aplicação."""

import os

from typing import List
from io import BytesIO
from langchain.schema.document import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

from constants import DATA_PATH
from src.controllers.vector_db import add_docs_to_chroma


def index_files(uploaded_files: List[BytesIO]) -> None:
    """Função que realiza a indexação de arquivos: carrega, divide e armazena no banco de dados vetorial."""

    # Criar lista de documentos carregados
    loaded_documents: List[Document] = []

    for file in uploaded_files:

        if file is not None:

            # obter metadados do arquivo
            filename = file.name
            filetype = file.type

            # criar caminho absoluto do arquivo
            filepath: str = os.path.abspath(os.path.join(DATA_PATH, filename))

            # se é PDF
            if filetype == "application/pdf":

                # abrir o arquivo usando o modo de abertura binário e salvar no diretório
                with open(filepath, "wb") as f:
                    f.write(file.getbuffer())

                # carregar e adicionar arquivo à lista
                pdf_loaded = PyPDFLoader(filepath).load()
                loaded_documents.extend(pdf_loaded)  # não usar append!

            # Se é arquivo de texto
            if filetype == "text/plain":

                # abrir o arquivo para escrita e salvar no diretório
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(file.getvalue().decode("utf-8"))

                # carregar e adicionar arquivo à lista
                txt_loaded = TextLoader(filepath, encoding="utf-8").load()
                loaded_documents.extend(txt_loaded)  # não usar append!

    # dividir documentos em pedaços
    chunks: list[Document] = split_documents(loaded_documents)

    # armazenar documentos no banco de dados vetorial
    add_docs_to_chroma(chunks)


def split_documents(documents: list[Document]) -> list[Document]:
    """Função responsável por dividir os documentos em pedaços menores (chunks)."""
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250,
        chunk_overlap=0
    )
    return text_splitter.split_documents(documents)


def get_list_of_uploaded_files() -> List[str]:
    """Função que retorna a lista de arquivos carregados pelo usuário."""
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    files = os.listdir(DATA_PATH)
    return [os.path.join(DATA_PATH, file) for file in files]


def delete_uploaded_files() -> str:
    """Função que apaga todos os arquivos carregados pelo usuário."""

    for filename in os.listdir(DATA_PATH):
        file_path = os.path.abspath(os.path.join(DATA_PATH, filename))
        if os.path.isfile(file_path):
            os.remove(file_path)
