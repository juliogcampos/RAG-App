"""Módulo responsável pela comunicação com a API do Ollama.
Documentação: https://github.com/ollama/ollama/blob/main/docs/api.md#api
"""

from typing import List
import requests
from constants import OLLAMA_MODELS_ENDPOINT


def list_of_Local_models() -> List:
    """Função que retorma a lista de modelos baixados pelo usuário com o Ollama."""

    response = requests.get(OLLAMA_MODELS_ENDPOINT)

    # verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        data = data["models"]

        list_of_local_models = []

        if len(data) > 0:
            for item in data:
                list_of_local_models.append(item["model"])

        list_of_local_models.sort()

        return list_of_local_models
    else:
        print(f'Ollama - Erro na requisição: {response.status_code}')
        return []
