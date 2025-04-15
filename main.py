from fastapi import FastAPI
from neo4j import GraphDatabase, basic_auth
app = FastAPI()



cypher_query = '''
MATCH (m:Movie {title:$movie})<-[:RATED]-(u:User)-[:RATED]->(rec:Movie)
RETURN distinct rec.title AS recommendation LIMIT 20
'''

@app.get("/")
async def root():
    driver = GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=basic_auth("neo4j", "password"),
    )

    with driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(cypher_query,
                              movie="Crimson Tide").data())
        for record in results:
            print(record['recommendation'])

    driver.close()
