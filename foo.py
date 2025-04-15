from neo4j import GraphDatabase

cypher_query = '''
MATCH (m:Movie {title:$movie})<-[:RATED]-(u:User)-[:RATED]->(rec:Movie)
RETURN distinct rec.title AS recommendation LIMIT 20
'''

driver = GraphDatabase.driver(
        "neo4j://172.23.240.1:7687",
        auth=("neo4j", "password"),
    )

with driver.session(database="neo4j") as session:
    results = session.execute_read(
        lambda tx: tx.run(cypher_query,
                          movie="Crimson Tide").data())
    for record in results:
        print(record['recommendation'])

driver.close()
