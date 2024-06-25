"""Módulo de construção da interface da barra lateral da aplicação."""

import streamlit as st

from src.views.streamlit.widgets import (
    show_file_uploader,
    show_select_llm,
    show_vector_db
)


def load_sidebar() -> None:
    """Função que exibe widgets na barra lateral."""

    # exibir widgets na barra lateral
    with st.sidebar:

        # mostrar widget para selecionar um LLM
        show_select_llm()

        # mostrar widget para carregar arquivos
        show_file_uploader()

        # mostrar widget do banco de dados vetorial
        show_vector_db()
