# RAG App

## Breve Descrição

![Interface do RAG App](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn7OdZIClBYfLTqmxIyupZtbM3URYZPPTBk8Wq9483IVD-75YAhiH7kd4xYxCyGl5MA4VKfxSZou3P9F_23cXAHJqtrM4PHy5jtGzLC8mFEG87i-w2migrmWdkwpAJ0H7mbN6c_WDqhW-8KsgNcRfH141Vwga1CRt97hCAHpZYokVBqpWmQ-aDTRycFClN/s1600/resposta.png)

O RAG App é uma aplicação de IA generativa que implementa a técnica de RAG (Retrieval-Augmented Generation) para adicionar dados privados a um LLM. Permite realizar pesquisas em documentos privados usando um grande modelo de linguagem (LLM) de código aberto.

A aplicação é direcionada para pesquisadores e usuários leigos. O sistema possui uma interface que possibilita ao usuário carregar documentos privados como arquivos de texto (.txt) e pdfs. Também permite que o usuário faça perguntas sobre os documentos carregados. O sistema gera respostas a partir de recuperação de informações contidas nos documentos.

Vale ressaltar que a aplicação foi desenvolvida para realizar RAG apenas em LLMs de código aberto. Outro ponto a ser considerado é que o programa condiciona o LLM a responder perguntas relacionadas apenas aos documentos carregados pelo usuário. Ele não permite que o modelo responda perguntas sobre informações que não estão presentes nos documentos.

O sistema foi desenvolvido em linguagem Python, com tecnologias e frameworks de código aberto que estão em constante evolução, acompanhando o estado da arte.

## Visão de Projeto

Esta seção descreve alguns cenários de uso para ilustrar possíveis interações do usuário com a aplicação.

### Cenário Positivo 1

João utiliza um modelo de linguagem de código aberto em uma empresa privada. Esse modelo não foi treinado com dados específicos da empresa em que ele trabalha. João deseja consultar um grande número de documentos em PDF para obter informações relevantes. Para isso, ele abre o aplicativo RAG, carrega os documentos no sistema e formula perguntas relacionadas aos documentos. Ele aguarda o processamento da pergunta e, em seguida, recebe a resposta na tela do computador.

---

### Cenário Positivo 2

Maria trabalha como pesquisadora em uma universidade e utiliza o ChatGPT para fazer consultas em seus documentos pessoais. Ela possui uma coleção de artigos acadêmicos, teses e relatórios armazenados em formato PDF. Para obter informações relevantes, Maria abre o aplicativo RAG, carrega seus documentos no sistema e formula perguntas relacionadas as suas pesquisas. Ela aguarda ansiosamente enquanto o sistema processa suas consultas e exibe as respostas na tela do computador.

---

### Cenário Negativo 1

Pedro é estudante e deseja utilizar o aplicativo RAG para consultar seus documentos pessoais. No entanto, ao tentar carregar os documentos, ele se depara com uma restrição: o sistema permite apenas o carregamento de arquivos nos formatos TXT e PDF. Infelizmente, os documentos de Pedro estão em formatos diferentes, como Word, planilhas e arquivos JSON. Ele fica frustrado por não conseguir utilizar o aplicativo da mesma forma que Maria e precisa encontrar uma solução alternativa para suas consultas.

---

### Cenário Negativo 2

Cíntia é uma advogada que utiliza o aplicativo RAG para consultar documentos jurídicos relevantes para seus casos. Ela carrega diversos contratos, petições e decisões judiciais no sistema e formula perguntas específicas relacionadas a esses documentos. No entanto, em uma ocasião, Cíntia faz uma pergunta sobre um assunto que não está abordado nos documentos carregados. Para sua surpresa, o sistema responde: "Não existem informações sobre os documentos consultados." Cíntia fica decepcionada, pois esperava encontrar alguma referência relevante, mas percebe que o aplicativo não conseguiu recuperar dados sobre o tema específico de sua pergunta.

---

### Cenário Negativo 3

Mário é um desenvolvedor de software que deseja utilizar o aplicativo "RAG" para aprimorar suas consultas em documentos técnicos. Ele está interessado em aproveitar os recursos avançados do GPT-4 para obter respostas mais precisas. No entanto, ao tentar baixar o GPT-4 no aplicativo, Mário descobre que a aplicação só funciona com modelos de linguagem de código aberto, como "Llama" e "Gemma". Ele fica surpreso e precisa reconsiderar sua estratégia para obter as informações desejadas.

## Documentação Técnica do Projeto

### Requisitos Funcionais

- **RF01**: Carregar arquivos. O sistema deve permitir ao usuário carregar arquivos nos formatos .txt e .pdf.
- **RF02**: Armazenar arquivos. O sistema deve armazenar os arquivos carregados no banco de dados vetorial.
- **RF03**: Selecionar um LLM. O sistema deve permitir ao usuário selecionar um LLM.
- **RF04**: Enviar pergunta. O sistema deve permitir que o usuário envie uma pergunta sobre os documentos carregados.
- **RF05**: Visualizar resposta. O sistema deve permitir que o usuário visualize a resposta feita à aplicação.
- **RF06**: Armazenar histórico de perguntas. O sistema deve armazenar na sessão de usuário as perguntas já respondidas pela aplicação.
- **RF07**: Visualizar contexto da resposta. O sistema deve permitir que o usuário visualize os fragmentos de documentos recuperados no banco de dados vetorial que foram utilizados pelo LLM como contexto para a elaboração da resposta.
- **RF08**: Limpar banco de dados vetorial. O sistema deve permitir que o usuário remova todos os documentos armazenados no banco de dados vetorial.

---

### Requisitos Não Funcionais

- **RNF01**: O sistema deve ser desenvolvido em linguagem Python.
- **RNF02**: O sistema deve possuir uma interface que facilite a interação do usuário com a aplicação.
- **RNF03**: O sistema deve ser integrado a uma ferramenta que permita executar grandes modelos de linguagem de código aberto em uma CPU.
- **RNF04**: O sistema deve utilizar o framework Langchain para simplificar a criação da aplicação usando LLMs.
- **RNF05**: O sistema deve utilizar um banco de dados vetorial de código aberto.

---

### Arquitetura de Software

A figura abaixo apresenta a estrutura principal da aplicação, incluindo seus componentes e relações. O RAG App é o componente central da arquitetura. Ele se conecta ao servidor local do Ollama por meio de uma REST API para obter dados sobre os modelos baixados pelo usuário. Essas informações são utilizadas para carregar a interface da aplicação, permitindo que o usuário selecione um modelo e envie perguntas. Além disso, o sistema é responsável pela criação de um banco de dados vetorial, onde os documentos carregados pelo usuário são armazenados em pedaços menores (chunks).

O Ollama é o componente responsável pelo processamento das consultas e geração de respostas com base no LLM. Essa ferramenta permite baixar grandes modelos de linguagem de código aberto e executá-los localmente.

![Arquitetura de software](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVEBTXynENBh8p_X7A4cPVqSBWpC697wmR1KY8KJpBe-KiReabE_j53ba0iMUVhWwqA9a5eifeczjL3lOdNJA77AHs3ZxcESdk4L0Q4pNTFZBFek7ccPB59VkmrytLx75d1NofwSJLw2-Pdf5DixW8cUq9mGUVQroEybpIoAxejE40Y0yEbdU8KLfS87y8/s1600/arquitetura.png)

---

### Diagrama de Casos de Uso

As funcionalidades da aplicação bem como a interação do usuário com elas são apresentadas na figura abaixo, que apresenta o diagrama de casos de uso. Na figura, é possível visualizar as interações do usuário com o sistema através de funcionalidades disponibilizadas pela aplicação.

![Diagrama de Casos de Uso](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5gjdIQ3KATIYHlm_fDSlxHW5UCrKeJkqhoAs52p2r5307EH_0TCCc9A2DfOGCJus1LxhqDoEpWEb20bjD4ZBsSnV1SzYwE9MIqQ6UBkzUYBwRGicMnbstgrU5DdK8nzspBNv6fvYvmUzD5gbGgWvWlmnpsBp1WOsKzlkfIGU_3dk5n2T0epriKxsQJhF6/s1600/diagrama_casos_de_uso.png)

---

### Tecnologias

- **[Ollama](https://ollama.com/)**: é uma ferramenta de código aberto que permite executar grandes modelos de linguagem (LLMs) de código aberto localmente. Para executar um LLM em um computador ou notebook é preciso ter pelo menos 8 GB de RAM disponível para rodar modelos de sete bilhões de parâmetros (7B).

- **[LangChain](https://www.langchain.com/)**: é um framework de código aberto projetado para simplificar a criação de aplicações usando grandes modelos de linguagem (LLMs).

- **[Chroma DB](https://www.trychroma.com/)**: é um banco de dados vetorial de código aberto que lida com a conversão documentos textuais em embeddings (representações numéricas) automaticamente. Ele é projetado especificamente para armazenar e recuperar embeddings eficientemente, permitindo pesquisas rápidas e precisas em documentos de texto.

- **[Streamlit](https://streamlit.io/)**: é uma biblioteca de código aberto que facilita a criação de aplicações web em Python sem exigir experiência de front-end.

---

### Testes

Foram realizados testes unitários, de integração e de interface na aplicação com a biblioteca **pytest**. A figura abaixo mostra o relatório de cobertura de testes gerado pela biblioteca **pytest-cov**. Com uma taxa geral de 95%, a maioria dos arquivos, funções e classes do código da aplicação foi testada.

![Cobertura de testes](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPwJu29kIzNJVOc3BzOlgSB9tSGp7C3VyymhnNF4a7qQH_q9NtceHmqVvqZZTqRDvFMGsdTW2QvZ_sl10074RL76sR2MbjPrDSfX8bLb1kSQQJtv-Blt-SbSD0a9huqkxwMedYOcphyphenhyphenUOq1wuDqz9GlOX168Xu5lk6RrPfGGkozkAhaPOOjrYzjxerxz4w/s1600/Captura%20de%20tela%202024-06-25%20094501.png)

---

### Manual de Utilização para Usuários Contemplados

```markdown
{ 
  Guia de Instruções:
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Para [Tarefa A: Carregar Arquivos] faça:
  Passo 1: O usuário navega até a interface de carregamento de arquivos.
  Passo 2: O usuário clica na área indicada para carregar arquivos".
  Passo 3: O sistema abre uma janela para o usuário selecionar um arquivo de seu dispositivo.
  Passo 4: O usuário seleciona um ou mais arquivos nos formatos .txt ou .pdf e clica em "Abrir".
  Passo 5: O usuário clica no botão "Enviar".
  Passo 6: O sistema exibe a mensagem "Carregando e adicionando arquivos ao banco".
  Passo 7: O sistema conclui o carregamento e armazenamento de arquivos e recarrega a página.

  Exceções ou potenciais problemas:
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Se [Condição Prevista C1: Arquivo em formato inválido]
     {
     Então faça: 
     Passo 1: Exibir mensagem de erro informando que o formato do arquivo não é suportado.
     É porque: O sistema só aceita arquivos nos formatos .txt e .pdf. 
     } 

  Para [Tarefa B: Armazenar Arquivos] faça:
  Passo 1: Após carregar o arquivo, o sistema processa e extrai o conteúdo do arquivo.
  Passo 2: O sistema converte o conteúdo em vetores.
  Passo 3: O sistema armazena esses vetores no banco de dados vetorial.
  Passo 4: O sistema exibe no widget do banco de dados vetorial o nome do arquivo carregado.

  Exceções ou potenciais problemas:
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Se [Condição Prevista C1: Falha ao processar o arquivo]
     {
     Então faça: 
     Passo 1: Exibir mensagem de erro ao usuário informando a falha.
     É porque: Pode haver problemas de leitura ou formatação no arquivo. 
     } 

  Para [Tarefa C: Selecionar um LLM] faça:
  Passo 1: O usuário acessa a interface de seleção de LLM.
  Passo 2: O usuário escolhe um LLM da lista fornecida.

  Para [Tarefa D: Enviar Pergunta] faça:
  Passo 1: O usuário navega até a interface de perguntas.
  Passo 2: O usuário insere a pergunta no campo apropriado.
  Passo 3: O usuário clica no botão "Enter" para enviar a pergunta.
  Passo 4: O sistema processa a pergunta e busca respostas no banco de dados vetorial utilizando o LLM selecionado.

  Exceções ou potenciais problemas:
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Se [Condição Prevista C1: LLM] não é capaz de responder a pergunta do usuário
     {
     Então faça: 
     Passo 1: Exibir mensagem ao usuário informando que não foi possível responder a pergunta.
     É porque: A pergunta pode estar mal formulada ou não foi possível encontrar informações sobre os documentos carregados. 
     } 

  Para [Tarefa E: Visualizar Resposta] faça:
  Passo 1: Após processar a pergunta, o sistema exibe a resposta na interface do usuário.
  Passo 2: O usuário visualiza a resposta apresentada.

  Para [Tarefa F: Visualizar Contexto da Resposta] faça:
  Passo 1: O sistema exibe a resposta ao usuário.
  Passo 2: Junto à resposta, o sistema apresenta os fragmentos de documentos utilizados como contexto.
  Passo 3: O usuário pode visualizar esses fragmentos para entender melhor a resposta.

  Para [Tarefa G: Armazenar Histórico de Perguntas] faça:
  Passo 1: Após responder a pergunta, o sistema armazena a pergunta e a resposta no histórico da sessão do usuário.
  Passo 2: O usuário pode visualizar o histórico de perguntas respondidas pela aplicação na interface.

  Para [Tarefa H: Limpar Banco de Dados Vetorial] faça:
  Passo 1: O usuário navega até a interface de gerenciamento do banco de dados vetorial.
  Passo 2: O usuário clica no botão "Limpar banco".
  Passo 3: O sistema remove todos os documentos do banco de dados vetorial.
  Passo 4: O sistema envia uma mensagem de confirmação para o usuário.
  Passo 5: O sistema recarrega a interface automaticamente.

  Exceções ou potenciais problemas:
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Se [Condição Prevista C1: Falha ao limpar o banco de dados]
     {
     Então faça: 
     Passo 1: Exibir mensagem de erro informando a falha na operação.
     É porque: Pode haver problemas de conexão ou permissões insuficientes. 
     } 
}
```

---

### Interface de Usuário

![Interface do RAG App](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJPl6vTw88jIYvX9ZHfLJZ8YEUimLT6vnHWWHdwUrWxY-BxbGmdzG2JC1cIF3umMW0noXzKH152qwHll29Q0O7VYOpSa9NAElx2tjDaSJVxEJkz2NYXFTNILvApApMDeJcYvjeiWR9oDTTmzTldEIEeF0C8Ye_UmX5_FJex29k8Ipk6vpQY6vIMi-irYfl/s1600/interface.png)
_Visão geral da aplicação_

![Interface do RAG App](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn7OdZIClBYfLTqmxIyupZtbM3URYZPPTBk8Wq9483IVD-75YAhiH7kd4xYxCyGl5MA4VKfxSZou3P9F_23cXAHJqtrM4PHy5jtGzLC8mFEG87i-w2migrmWdkwpAJ0H7mbN6c_WDqhW-8KsgNcRfH141Vwga1CRt97hCAHpZYokVBqpWmQ-aDTRycFClN/s1600/resposta.png)
_Visão de uma resposta do sistema_

![Visualização de contexto da resposta](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0g4gD-xr65NXRrhnyj45Imy6xADlGCWVoXREdsjGeknR1PYS92EAI46_lw_uab550HrMRpNo2MykEww8HO0BR1COVnpDFF1NREPZKePQj-qfgNB1gHnGEXimvur1YSfJM_s0yc9asabl91VaexqZsvzCHNttpgXnwfPrGNifhhDmjqZapnqxd7EE0L64v/s1600/contexto_da_resposta.png)
_Visão do contexto de uma resposta_
