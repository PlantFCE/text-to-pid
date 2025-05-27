from py2neo import Node, Relationship
from config import graph

graph.delete_all() # Clear old data

# Create P&ID equipment as nodes in the database
pump = Node("Pump", name="P-101")
pipe = Node("Pipe", name="Outlet Pipe")
tank = Node("Tank", name="Feed Tank")
pgauge = Node("PressureGauge", name="PG-101")

# Define relationships (piping and measurement)
flow1 = Relationship(pump, "FLOWS_TO", pipe)
flow2 = Relationship(pipe, "FLOWS_TO", tank)
measures = Relationship(pgauge, "MEASURES", pipe)

graph.create(pump | pipe | tank | pgauge | flow1 | flow2 | measures)

print("Nodes added into Neo4j.")