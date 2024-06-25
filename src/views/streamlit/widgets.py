"""Módulo que armazena funções de gerenciamento de widgets da aplicação."""

from typing import List
import streamlit as st

from constants import UPLOADED_FILES
from src.controllers.ollama import list_of_Local_models
from src.controllers.files import index_files
from src.controllers.vector_db import clear_chroma_db
from src.controllers.files import get_list_of_uploaded_files, delete_uploaded_files
from src.views.streamlit.session_state import set_llm_name, clean_input_question


def show_select_llm() -> None:
    """Finção que exibe widget para selecionar um LLM."""

    with st.form(key="select_llm"):

        # lista de modelos baixados com o Ollama
        models: List = list_of_Local_models()

        st.subheader("🤖 LLM")

        # selecionar LLM
        selected_llm = st.selectbox(
            "Selecione um modelo:", models,
            key="select_llm",
        )

        # salvar nome da llm selecionada na sessão de estado
        set_llm_name(selected_llm)

        # botão de submeter
        submit_btn = st.form_submit_button("Selecionar", type="primary", disabled=True)

        if submit_btn:
            st.toast(f"Modelo '{selected_llm}' selecionado.")


def show_file_uploader() -> None:
    """Função que exibe widget para carregar arquivos."""

    with st.form("upload_docs"):

        st.subheader("⬆️ Carregar arquivos")

        # realizar upload de arquivos
        uploaded_files: List = st.file_uploader(
            label="Carregar arquivos",
            type=["pdf", "txt"],
            accept_multiple_files=True,
            key="file_uploader",
        )

        # botão de submeter
        submitted = st.form_submit_button("Enviar")

        if submitted:
            if len(uploaded_files) == 0:
                st.toast("Carregue um documento antes de enviar!")

            with st.spinner("Carregando e adicionando arquivos ao banco..."):
                index_files(uploaded_files)

        # atualizar lista de arquivos carregados com os novos arquivos
        st.session_state[UPLOADED_FILES] = get_list_of_uploaded_files()


def show_vector_db() -> None:
    """Função que exibe widget do banco de dados vetorial."""

    with st.container(border=True):

        st.subheader("📦 Banco de dados vetorial")

        # exibir lista de arquivos carregados
        uploaded_files = st.session_state[UPLOADED_FILES]
        st.text("Arquivos:")
        st.write(uploaded_files)

        # botão para limpar banco vetorial
        button = st.button("Limpar banco", key="clean_db")
        if button:

            # deletar arquivos carregados
            delete_uploaded_files()

            # limpar lista de arquivos carregados da sessão de usuário
            st.session_state[UPLOADED_FILES] = []

            # limpar input da questão do usuário
            clean_input_question()

            # limpar banco de dados vetorial
            response = clear_chroma_db()
            st.toast(response)

            # recarregar página
            st.rerun()
