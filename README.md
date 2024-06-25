# RAG App

- O RAG App é uma aplicação de IA generativa que implementa a técnica de RAG (Retrieval-Augmented Generation) para adicionar dados privados a um LLM de código aberto. O sistema foi desenvolvido em linguagem Python, com tecnologias e frameworks de código aberto.

## 1 - Pré-requisitos

- Para executar a aplicação é necessário possuir um computador com no mínimo 8GB de memória RAM.
- A aplicação foi desenvolvida em Python na versão 3.11.9. Recomenda-se utilizar uma versão do Python acima de 3.7 para melhor compatibilidade. Abra o terminal e verifique a versão do Python instalada em seu computador com o comando abaixo:

```console
python --version
```

## 2 - Instalação

### Ollama

- Faça o download do **Ollama** em: <https://ollama.com/> e instale o arquivo executável normalmente.
- Abra o prompt de comando (terminal) e execute o código abaixo para baixar o **Meta Llama 3** para o seu computador:

```console
ollama pull llama3
```

- Ainda no terminal, execute o código abaixo para baixar o **Gemma** para o seu computador:

```console
ollama pull gemma
```

- Execute o comando abaixo para visualizar os modelos baixados para sua máquina com o Ollama:

```bash
ollama list
```

- Veja a lista de outros modelos disponíveis para download em: <https://ollama.com/library>

### Dependências da Aplicação

- Abra o prompt de comando e execute o código abaixo para instalar todas as dependências da aplicação:

```console
.\install
```

- Sempre que adicionar uma nova dependência à aplicação, execute o comando abaixo:

```python
pip freeze > requirements.txt
```

- Caso seja necessário desinstalar todas as dependências, execute o comando abaixo:

```python
pip uninstall -r requirements.txt -y
```

## 3 - Execução

- Abra o terminal e execute o código abaixo para ativar o ambiente virtual **.venv** da aplicação:

```console
.venv\scripts\activate
```

- Execute o comando abaixo para executar a aplicação:

```python
streamlit run app.py
```

## 4 - Testes

- Para executar os testes unitários e de integração da aplicação, execute o comando abaixo no terminal:

```python
pytest
```

- Para executar apenas o módulo de testes unitários, execute o comando abaixo:

```python
pytest test/test_1_unitary_tests.py
```

- Para executar apenas o módulo de testes de integração, execute o comando abaixo:

```python
pytest test/test_2_integration_tests.py
```

- Para executar os testes e gerar relatório de cobertura, execute o comando abaixo:

```python
pytest --cov=. --cov-report html
```

- Abra o arquivo **index.html** na pasta **htmlcov**, localizada no diretório raiz do projeto, para visualizar o relatório de cobertura de testes.

# 5 - Documentação

Visite a wiki do projeto para ler a documentação: <https://github.com/juliogcampos/RAG-App/wiki>
