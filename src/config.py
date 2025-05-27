from py2neo import Graph

NEO4J_URL = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASS = "password"

graph = Graph(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASS))
