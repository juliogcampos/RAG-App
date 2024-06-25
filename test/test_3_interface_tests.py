"""Módulo de testes de interface da aplicação com Stremlit.
Documentação: https://docs.streamlit.io/develop/api-reference/app-testing """

from streamlit.testing.v1 import AppTest
from constants import APP_PATH

def test_run():
    """Teste que simula a aplicação em execução."""

    app = AppTest.from_file(APP_PATH)
    assert not app.exception