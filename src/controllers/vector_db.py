import os
from typing import List

from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma

from constants import CHROMA_PATH
from src.controllers.embeddings import get_default_text_embedding


def get_chroma_db() -> Chroma:
    """Função que retorna a instância do Chroma e cria o banco se não existir.

    Returns:
        Chroma: instância do Chroma, banco de dados vetorial.
    """
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_default_text_embedding()
    )
    return db


def add_docs_to_chroma(chunks: list[Document]) -> None:
    """Função que adiciona documentos ao banco de dados vetorial se ainda não foram carregados.

    Args:
        chunks (list[Document]): Lista de pedaços de documentos para adicionar ao banco vetorial.
    """

    # Carregar base de dados existente
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_default_text_embedding()
    )

    # Adicionar ou atualizar documentos
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"🔎 Número de documentos do banco vetorial: {len(existing_ids)}")

    # Obter ids dos chunks
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Adicionar documentos apenas se não existirem no banco.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"🗒️  Adicionando novos documentos: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        print("⚠️  Nenhum documento novo para adicionar")


def calculate_chunk_ids(chunks: list[Document]) -> List[Document]:
    """Função que gera um identificador para cada pedaço de um documento.

    Examples:
        -   Exemplo de um identificador criado: "data/monopoly.pdf:6:2"
            documento : número da página : índice do chunk.

    Args:
        chunks (list[Document]): Lista de pedaços de documentos.

    Returns:
        List[Document]: Lista de pedaços de documentos com identificadores.
    """

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # Se o ID da página for igual ao anterior, incrementar o índice
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calcula o ID do chunk (pedaço de documento)
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Adiciona o id aos metadados da página.
        chunk.metadata["id"] = chunk_id

    return chunks


def clear_chroma_db() -> str:
    """Função que limpa o banco de dados vetorial do Chroma.

    Returns:
        str: Mensagem de sucesso.
    """

    chroma_db = get_chroma_db()
    chroma_db.delete_collection()

    return "Banco de dados vetorial limpo!"


def get_docs_of_chroma() -> List:
    """Método que retorna a lista de documentos persistidos no Chroma, banco de dados vetorial.

    Returns:
        List: lista de documentos persistidos no Chroma.
    """

    # obter banco persistido
    db = get_chroma_db()

    # obter todos os documentos e metadados do Chroma
    data = db.get()

    # lista de documentos
    docs = []

    # obter apenas os nomes dos arquivos fonte
    for doc in data['metadatas']:
        source = os.path.basename(doc['source'])
        if source not in docs:
            docs.append(source)

    return docs
