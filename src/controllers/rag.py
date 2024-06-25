"""Módulo que executa uma consulta a uma LLM usando a técnica de RAG."""

# import os
# variáveis de ambiente para usar o LangSmith
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
# os.environ["LANGCHAIN_API_KEY"] = ""  # adicione sua API KEY

from typing import Dict

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.llms.ollama import Ollama

from constants import CHROMA_PATH
from src.controllers.prompts import PROMPT_TEMPLATE
from src.controllers.embeddings import get_default_text_embedding
from src.controllers.vector_db import get_chroma_db


def rag_chat(llm_name: str, question: str, prompt_template: str) -> Dict:
    """Função que executa uma consulta a uma LLM usando a técnica de RAG.

    Docs:
        Create retrieval chain: 
            - https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html
            - https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval.create_retrieval_chain.html

    Args:
        llm_name (str): Nome do modelo da LLM.
        question (str): Pergunta do usuário.
        prompt_template (str): Modelo de prompt.

    Returns:
        _type_: Resposta gerada pela LLM a partir de dados adicionais fornecidos como contexto.
    """
    # Retorna o banco Chroma criado localmente
    vector_db = get_chroma_db()

    # Criar recuperador de documentos e definir quantidade de documentos recuperados igual a 5
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    # Cria um modelo Ollama com especificações definidas
    # Define a temperatura do llm como 0 para respostas mais precisas
    llm = Ollama(model=llm_name, temperature=0)

    # Crie um modelo de prompt de bate-papo
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", prompt_template),
            ("human", "{input}"),
        ]
    )

    # Criar cadeia para passar uma lista de documentos para um modelo
    question_answer_chain = create_stuff_documents_chain(llm, prompt)

    # Criar uma cadeia de recuperação de documentos
    chain = create_retrieval_chain(retriever, question_answer_chain)

    # Executar a cadeia
    response = chain.invoke({"input": question})

    return response
