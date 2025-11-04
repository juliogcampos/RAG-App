"""Módulo de construção do conteúdo do elemento principal da aplicação."""

from typing import List, Dict
import streamlit as st

from src.controllers.prompts import PROMPT_TEMPLATE_BASE, PROMPT_TEMPLATE_FOR_RAG
from src.controllers.rag import rag_chat
from src.controllers.ollama import chat_to_llm
from src.views.streamlit.templates import create_card
from src.views.streamlit.widgets import get_list_of_uploaded_files
from src.views.streamlit.session_state import (
    get_questions_and_answers,
    get_llm_name,
    save_question_and_answer
)


def load_main() -> None:
    """Função que carrega página principal e permite ao usuário fazer RAG nos documentos carregados."""

    # exibir input da pergunta
    question = st.text_input(
        label="Digite uma pergunta ou comando",
        label_visibility="hidden",
        placeholder="Digite uma pergunta ou comando",
        key="input_question"
    )

    # Se input não estiver vazio e o enter for pressionado
    if question:

        # obter a llm selecionada pelo usuário
        llm_name = get_llm_name()

        # obter lista de documentos adicionados pelo usuário
        list_of_uploaded_files = get_list_of_uploaded_files()
        if len(list_of_uploaded_files) == 0:

            # Respondendo perguntas usando o conhecimento do LLM
            with st.spinner("Respondendo a pergunta com dados de treinamento do LLM..."):

                # fazer pergunta ao LLM sem RAG
                response: Dict = chat_to_llm(llm_name=llm_name, question=question, prompt_template=PROMPT_TEMPLATE_BASE)
                handle_response(response)

        else:

            # Respondendo perguntas usando apenas as informações dos documentos
            with st.spinner("Respondendo a pergunta com dados do(s) documento(s)..."):

                # fazer pergunta ao LLM usando RAG
                response: Dict = rag_chat(llm_name=llm_name, question=question, prompt_template=PROMPT_TEMPLATE_FOR_RAG)
                handle_response(response)


def handle_response(response):
    """Função que salva a resposta de uma questão do usuário e exibe na interface."""

    # armazenar pergunta e resposta no estado da sessão
    save_question_and_answer(response)

    # obter lista de questões
    questions: List = get_questions_and_answers()

    for index, item in enumerate(reversed(questions)):

        input = item["input"]
        answer = item["answer"]
        context = item["context"]

        # armazenar documentos recuperados pelo RAG
        docs = []

        # extrair metadados dos documentos de contexto
        for doc in context:
            docs.append(doc.__dict__)

        if index == 0:
            # exibir card da última questão com streaming
            create_card(
                title=input,
                content=answer,
                streaming=True,
                footer_title="Documentos consultados",
                footer=docs
            )
        else:
            # exibir card das outras questões respondidas sem streaming
            create_card(
                title=input,
                content=answer,
                streaming=False,
                footer_title="Ver documentos encontrados",
                footer=docs
            )
