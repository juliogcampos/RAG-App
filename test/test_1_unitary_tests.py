"""Módulo de testes unitários da aplicação desenvolvidos com Pytest."""

from typing import List
from src.controllers.rag import rag_chat
from src.controllers.vector_db import clear_chroma_db
from src.controllers.prompts import PROMPT_TEMPLATE, guided_prompt_template


def test_answer_format():
    """Teste que verifica formato da resposta da consulta a LLM usando RAG."""

    llm_name = 'llama3'
    question = 'O que é RAG?'

    # executar consulta
    result = rag_chat(llm_name, question, PROMPT_TEMPLATE)
    print(result)

    assert isinstance(result["answer"], str), "A resposta deve ser uma string"
    assert isinstance(result["context"], List), "As fontes devem estar em uma lista"


def test_data_not_found():
    """Teste que verifica resposta da LLM quando dados de contexto não são encontrados."""

    llm_name = 'gemma'
    question = 'O que é RAG?'

    # limpar banco vetorial
    clear_chroma_db()

    # executar consulta
    result = rag_chat(llm_name, question, PROMPT_TEMPLATE)
    print(result)

    assert 'Não' or 'não' in result["answer"], "A resposta deve conter a palavra 'não'"


def test_sources_not_found():
    """Teste que verifica resposta da LLM quando dados de fontes não são encontrados."""

    llm_name = 'llama3'
    question = 'O que é RAG?'

    # limpar banco vetorial
    clear_chroma_db()

    # executar consulta
    result = rag_chat(llm_name, question, PROMPT_TEMPLATE)
    print(result)

    assert len(result["context"]) == 0, "A lista de fontes deve ter tamanho 0"


def test_false_answer():
    """Teste que condiciona a LLM a responder 'False' independente dos documentos recuperados no RAG."""

    llm_name = 'gemma'
    question = 'O que é RAG?'

    # usar modelo de prompt que condiciona a LLM a responder sempre 'False'
    prompt_template = guided_prompt_template('False')

    # executar consulta
    result = rag_chat(llm_name, question, prompt_template)
    print(result)

    assert 'False' in result["answer"], "A resposta deve conter a palavra 'False'"


def test_true_answer():
    """Teste que condiciona a LLM a responder 'True' independente dos documentos recuperados no RAG."""

    llm_name = 'llama3'
    question = 'O que é RAG?'

    # usar modelo de prompt que condiciona a LLM a responder sempre 'True'
    prompt_template = guided_prompt_template('True')

    # executar consulta
    result = rag_chat(llm_name, question, prompt_template)
    print(result)

    assert 'True' in result["answer"], "A resposta deve conter a palavra 'True'"


def test_null_answer():
    """Teste que condiciona a LLM a responder 'Null' independente dos documentos recuperados no RAG."""

    llm_name = 'gemma'
    question = 'O que é RAG?'

    # usar modelo de prompt que condiciona a LLM a responder sempre 'Null'
    prompt_template = guided_prompt_template('Null')

    # executar consulta
    result = rag_chat(llm_name, question, prompt_template)
    print(result)

    assert 'Null' in result["answer"], "A resposta deve conter a palavra 'Null'"


def test_empty_answer():
    """Teste que condiciona a LLM a responder '' independente dos documentos recuperados no RAG."""

    llm_name = 'llama3'
    question = 'O que é RAG?'

    # usar modelo de prompt que condiciona a LLM a responder sempre ''
    prompt_template = guided_prompt_template('')

    # executar consulta
    result = rag_chat(llm_name, question, prompt_template)
    print(result)

    assert '' in result["answer"], "A resposta deve retornar uma string vazia"
