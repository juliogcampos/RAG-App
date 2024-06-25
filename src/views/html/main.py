"""Módulo de construção do conteúdo do elemento principal da aplicação."""

from typing import List, Dict
import streamlit as st

from src.controllers.prompts import PROMPT_TEMPLATE
from src.controllers.rag import rag_chat
from src.views.streamlit.templates import create_card
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
        with st.spinner("Realizando busca nos documentos..."):

            # obter a llm selecionada pelo usuário
            llm_name = get_llm_name()

            # fazer pergunta à llm usando RAG e armazenar a resposta
            response: Dict = rag_chat(llm_name=llm_name, question=question, prompt_template=PROMPT_TEMPLATE)

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
                    # exibir card de última questão com streaming
                    create_card(
                        title=input,
                        content=answer,
                        streaming=True,
                        footer_title="Ver documentos encontrados",
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
