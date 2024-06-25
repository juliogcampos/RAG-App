"""Módulo que armazena templates de componentes para o Streamlit."""

from typing import List

import streamlit as st
import time


def stream_data(data: List):
    """Função que simula um streaming de dados.

    Args:
        data (List): Lista com palavras para simular um streaming.

    Yields:
        word (str): palavra a ser exibida na interface como um streaming.
    """
    for word in data:
        yield word + " "
        time.sleep(0.1)


def create_card(title: str, content: str, streaming: bool, footer_title: str, footer: str) -> None:
    """Função que cria um template de um card.

    Args:
        title (str): Título do card.
        content (str): Conteúdo do card.
        streaming (bool): Indica se o conteúdo deve ser exibido como streaming.
        footer_title (str): Título do rodapé do card.
        footer (str): Conteúdo do rodapé do card.
    """

    # criar um container para o card
    card = st.container(border=True)

    # adicionar elementos ao card
    with card:
        st.subheader(title)

        # exibir conteúdo como streaming
        if streaming:
            content = content.split(" ")
            st.write_stream(stream_data(content))
        else:
            # exibir conteúdo sem streaming
            st.write(content)

        # elemento que pode ser expandido/recolhido
        with st.expander(footer_title):
            st.write(footer)
