"""Módulo que armazena funções de estado de sessão de usuário.
Documentação: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state"""

from typing import List, Dict
import streamlit as st

from src.controllers.files import get_list_of_uploaded_files
from constants import QUESTION, QUESTIONS, LLM_NAME, UPLOADED_FILES


def start_session_state() -> None:
    """Função que inicializa chaves de estados de sessão de usuário."""

    if LLM_NAME not in st.session_state:
        st.session_state[LLM_NAME] = []

    if QUESTION not in st.session_state:
        st.session_state[QUESTION] = ''

    if QUESTIONS not in st.session_state:
        st.session_state[QUESTIONS] = []

    if UPLOADED_FILES not in st.session_state:
        st.session_state[UPLOADED_FILES] = get_list_of_uploaded_files()


def get_llm_name() -> str:
    """Função que retorna o nome da llm armazenada na sessão do usuário."""
    return st.session_state[LLM_NAME]


def set_llm_name(name: str) -> None:
    """Função que altera o nome da llm n estado de sessão do usuário."""
    st.session_state[LLM_NAME] = name


def get_questions_and_answers() -> List:
    """Função que retorna a lista de perguntas e respostas do usuário realizadas na sessão."""
    return st.session_state[QUESTIONS]


def save_question_and_answer(response: Dict) -> None:
    """Função que salva a resposta de uma pergunta no estado de sessão."""
    st.session_state[QUESTIONS].append(response)


def clean_input_question() -> None:
    """Função que limpa o input que armazena a questão do usuário."""
    st.session_state[QUESTION] = st.session_state["input_question"]
    st.session_state["input_question"] = ''
