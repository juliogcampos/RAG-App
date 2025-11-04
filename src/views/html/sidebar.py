"""Módulo de construção da interface da barra lateral da aplicação."""

import streamlit as st

from src.views.streamlit.widgets import (
    file_uploader,
    select_llm,
    vector_db
)


def load_sidebar() -> None:
    """Função que exibe widgets na barra lateral."""

    # exibir widgets na barra lateral
    with st.sidebar:

        # mostrar widget para selecionar um LLM
        select_llm()

        # mostrar widget para carregar arquivos
        file_uploader()

        # mostrar widget do banco de dados vetorial
        vector_db()
