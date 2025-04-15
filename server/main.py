from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase, basic_auth
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique: ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexão com o Neo4j
driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=basic_auth("neo4j", "password"),
)


# Endpoint 1: Busca por filmes com título parecido
@app.get("/search", response_model=List[str])
async def search_movies(query: str = Query(..., min_length=1)):
    cypher = '''
    MATCH (m:Movie)
    WHERE toLower(m.title) CONTAINS toLower($query)
    RETURN DISTINCT m.title AS title
    LIMIT 20
    '''
    with driver.session(database="neo4j") as session:
        results = session.execute_read(
            lambda tx: tx.run(cypher, {"query": query}).data()
        )
    return [record["title"] for record in results]


# Endpoint 2: Detalhes de um filme específico (retorna todos os dados)
@app.get("/movie/{title}")
async def get_movie(title: str):
    cypher = '''
    MATCH (m:Movie {title: $title})
    RETURN m AS movie
    '''
    with driver.session(database="neo4j") as session:
        result = session.execute_read(
            lambda tx: tx.run(cypher, title=title).single()
        )
    if result:
        movie_data = result["movie"].items()  # Extrai todos os dados do nó
        return {key: value for key, value in movie_data}
    return {"error": "Movie not found"}


# Endpoint 3: Recomendações de filmes semelhantes (com mais dados)
@app.get("/recommendations/{title}")
async def recommend_movies(title: str):
    cypher = '''
    MATCH (m:Movie {title: $title})-[:ACTED_IN|IN_GENRE|DIRECTED*2]-(rec:Movie)
    WHERE m <> rec
    RETURN DISTINCT rec.title AS title, rec.poster AS poster, rec.released AS released
    LIMIT 25
    '''
    with driver.session(database="neo4j") as session:
        results = session.execute_read(
            lambda tx: tx.run(cypher, title=title).data()
        )

    # Ajuste de estrutura para retornar um dicionário de dados mais detalhados
    recommendations = [
        {"title": record["title"], "poster": record.get("poster", "No poster"),
         "released": record.get("released", "Unknown")}
        for record in results
    ]

    return recommendations
