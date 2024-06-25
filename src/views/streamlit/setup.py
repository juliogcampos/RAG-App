"""Módulo que aplica configurações à página da aplicação."""

import streamlit as st

from streamlit.components.v1 import html

from constants import CSS_PATH
from src.views.streamlit.session_state import start_session_state


def setup_page(title: str) -> None:
    """Função que configura a página da aplicação."""

    st.set_page_config(
        page_title=title,
        page_icon="📝",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None
    )

    # criar título
    st.title(title)
    st.markdown("---")

    # caregar CSS
    load_css()

    # executar scripts
    execute_scripts()

    # inicializar estado de sessão
    start_session_state()


def load_css() -> None:
    """Função que carrega folha de estilo à aplicação."""
    with open(CSS_PATH, encoding="utf-8") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)


def execute_scripts() -> None:
    """Função que carrega scripts do JavaScript na página da aplicação."""
    scripts = """
    <script>
        'use strict';
        console.log("script em execução ...");
    </script>
    """
    # Usando o componente HTML para injetar o script na página
    html(scripts, height=0)
