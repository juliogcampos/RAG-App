"""Módulo que armazena funções para enviar mensagens na interface de usuário."""

import time
import streamlit as st


def send_success_msg(message: str) -> None:
    """Função que envia uma mensagem temporária de sucesso."""
    msg = st.success(message, icon="✅")
    clear_msg(msg)


def send_error_msg(message: str) -> None:
    """Função que envia uma mensagem temporária de erro."""
    msg = st.error(message, icon="❌")
    clear_msg(msg)


def send_warning_msg(message: str) -> None:
    """Função que envia uma mensagem temporária de aviso."""
    msg = st.warning(message, icon="⚠️")
    clear_msg(msg)


def send_info_msg(message: str) -> None:
    """Função que envia uma mensagem temporária de informação."""
    msg = st.info(message, icon="ℹ️")
    clear_msg(msg)


def clear_msg(message: str) -> None:
    """Função que limpa uma mensagem enviada após 2 segundos."""
    time.sleep(2)  # esperar 2 segundos
    message.empty()  # limpar a mensagem
