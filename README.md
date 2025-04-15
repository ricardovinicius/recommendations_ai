# 🎬 Movie Recommender System

Um sistema simples de recomendação de filmes usando **FastAPI**, **Vue 3** com **Vuetify** e **Neo4j**. O sistema permite:

- 🔍 Buscar por filmes com base no título.
- 📄 Ver detalhes de um filme específico.
- 🤝 Receber recomendações de filmes similares com base em conexões no grafo.

---

## 🛠 Tecnologias Utilizadas

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) — Framework web rápido e moderno.
- [Neo4j](https://neo4j.com/) — Banco de dados orientado a grafos.
- [Neo4j Python Driver](https://neo4j.com/docs/api/python-driver/current/) — Driver oficial para Python.

### Frontend
- [Vue 3 + Vite](https://vitejs.dev/)
- [Vuetify 3](https://next.vuetifyjs.com/) — Framework de UI baseado em Material Design.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.10+
- Node.js 18+
- Neo4j 5.x (ou compatível)

---

## 🧱 Como Configurar o Neo4j

1. Baixe e instale o Neo4j:
   - [Guia de instalação oficial](https://neo4j.com/docs/operations-manual/current/installation/)

2. Execute o Neo4j Desktop ou inicie via linha de comando.

3. Crie um banco de dados chamado `neo4j` (ou ajuste o nome no código).

4. Defina um usuário e senha. Por padrão, use:
   ```python
   auth=basic_auth("neo4j", "password")
   ```

5. Carregue os dados de exemplo:

   Você pode usar o repositório oficial da Neo4j com um grafo de filmes e recomendações para isso:

   👉 [neo4j-graph-examples/recommendations](https://github.com/neo4j-graph-examples/recommendations)

   Siga as instruções de importação para popular seu banco com filmes, atores, diretores, etc.

---

## 📡 Endpoints da API

### `GET /search?query=Matrix`
Retorna uma lista de títulos de filmes que contêm o termo de busca.

### `GET /movie/{title}`
Retorna os dados completos de um filme específico (ex: orçamento, receita, duração, idiomas, etc).

### `GET /recommendations/{title}`
Retorna uma lista de filmes recomendados com base nas conexões do grafo (atores, gêneros, diretores).

---

## 🧪 Exemplo de Fluxo

1. O usuário digita “Matrix” no campo de busca.
2. O frontend sugere resultados com base no endpoint `/search`.
3. O usuário seleciona “The Matrix”.
4. O frontend mostra os detalhes do filme (usando `/movie/{title}`).
5. Abaixo, recomendações de filmes são exibidas (via `/recommendations/{title}`).
6. O usuário pode clicar em qualquer filme recomendado para repetir o ciclo.

