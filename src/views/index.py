"""Módulo de construção da interface da aplicação."""

from src.views.html.main import load_main
from src.views.html.sidebar import load_sidebar
from src.views.streamlit.setup import setup_page


def start_app() -> None:
    """Função que constrói e carrega a interface da aplicação."""

    # configurar página da aplicação
    setup_page(title="RAG App")

    # carregar a barra lateral
    load_sidebar()

    # carregar conteúdo da página principal
    load_main()
