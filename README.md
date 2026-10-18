# Quiz de estatística | Avaliação interativa

Questionário de estatística com identificação do participante, correção das respostas e persistência em SQLite.

**Aplicações Python** · Aplicação Streamlit

[← Portfólio de Thiago Oliveira](https://github.com/thiagoramos20042/thiagoramos20042) · [Catálogo de projetos](https://github.com/thiagoramos20042/thiagoramos20042/blob/main/PROJETOS.md)

## Objetivo

Reunir aplicação do teste e registro de desempenho em uma interface simples.

## O que você encontra

- Cadastro de nome, idade e função do participante.
- Questionário com cálculo de acertos.
- Gravação dos resultados no banco local.

## Tecnologias

Python · Streamlit · SQLite

## Arquivos principais

| Arquivo | Conteúdo |
| --- | --- |
| [final.py](final.py) | Interface, perguntas, correção e gravação dos resultados. |
| [requirements.txt](requirements.txt) | Registro das dependências do ambiente original. |

## Como explorar

Na raiz do repositório, em um ambiente Python separado:

```bash
python -m pip install streamlit
python -m streamlit run final.py
```

## Contexto do projeto

O arquivo de entrada é final.py. O banco local respostas.db é usado para persistir as respostas.

---

Integra o [portfólio de Thiago Oliveira](https://github.com/thiagoramos20042).
