@echo off
rem Script de instalação de dependências do projeto

rem Define a página de código para UTF-8
chcp 65001 > nul

rem Verifica se o ambiente virtual já existe
if exist .venv (
    echo Ambiente virtual '.venv' já criado.
) else (
    echo Criando o ambiente virtual '.venv' ...
    python -m venv .venv
)

rem Ativa o ambiente virtual
call .venv\Scripts\activate

rem Verifica se o arquivo requirements.txt existe
if exist requirements.txt (
    echo Instalando as dependências do projeto...
    pip install -r requirements.txt
    echo As dependências do projeto foram instaladas com sucesso!
) else (
    echo Criando arquivo 'requirements.txt'...
    break > "requirements.txt"
)

pause