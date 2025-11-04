"""Módulo responsável pela comunicação com a API do Ollama.
Documentação: https://github.com/ollama/ollama/blob/main/docs/api.md#api
"""

import requests
from typing import Dict, List

from constants import OLLAMA_MODELS_ENDPOINT

from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate

"""Módulo que executa uma consulta a um LLM."""


def chat_to_llm(llm_name: str, question: str, prompt_template: str) -> Dict:
    """Função que executa uma consulta a uma LLM.

    Args:
        llm_name (str): Nome do modelo da LLM.
        question (str): Pergunta do usuário.
        prompt_template (str): Modelo de prompt.

    Returns:
        Dict: Resposta gerada pela LLM a partir de dados adicionais fornecidos como contexto.
    """

    # Cria instância do Ollama com especificações definidas
    # Definir a temperatura do LLM como 0 para respostas mais precisas
    llm = Ollama(model=llm_name, temperature=0)

    # Criar um modelo de prompt de bate-papo
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", prompt_template),
            ("human", "Context: {context}"),
            ("human", "Question: {input}"),
        ]
    )

    # Criar a cadeia
    chain = prompt | llm

    # Executar a cadeia
    response = chain.invoke({"context": "", "input": question})

    # retornar resposta estruturada, igual a do rag_chat (src.controllers.rag import rag_chat)
    return {"input": question, "answer": response, "context": ""}


def list_of_Local_models() -> List:
    """Função que retorma a lista de modelos baixados pelo usuário com o Ollama."""

    response = requests.get(OLLAMA_MODELS_ENDPOINT)

    # verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        data = data["models"]

        list_of_local_models = []

        if len(data) > 0:
            for item in data:

                # remove modelos de incorporação (nomic)
                if "nomic" not in item["model"]:
                    list_of_local_models.append(item["model"])

        list_of_local_models.sort()

        return list_of_local_models
    else:
        print(f'Ollama - Erro na requisição: {response.status_code}')
        return []
