"""Módulo que armazena modelos de prompt utilizados na LLM."""

from typing import Tuple

PROMPT_TEMPLATE: Tuple = (
    "Answer the question in Portuguese based only on the context below."
    "If you don't know the answer, just say that you didn't find the information in the documents."
    "Don't try to generate a response."
    "Context: {context}"
)


QA_SYSTEM_PROMPT: str = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Answer the question in Portuguese.\

{context}"""


def guided_prompt_template(response: str) -> str:
    """Função que gera um modelo de prompt que orienta a LLM a retornar sempre uma determinada resposta, independente do contexto adicionado."""

    prompt: str = f"""Always answer the question with {response}, regardless of the context.

        Context: {{context}}
    """
    return prompt
