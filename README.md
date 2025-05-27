<img src="images/logo.svg" style="width: 100%">

# <center>Text to P&ID</center>

Text to P&ID aims to convert a process description to P&ID.

## Overview
The process is as follows:
- Extract equipment/instruments from process description using Natural Language Processing, and understand the relations between them.
- Store the above as a graph in a DBMS like [Neo4j](http://neo4j.com/).
- Evaluate different implementations, enumerating the position of equipment, to find the best implementation.
- Create a [DEXPI](https://dexpi.org/) XML file.
- Validate a P&ID against a set of rules by running Cypher queries against the Neo4j database.

## Extracting Equipment/Instruments

We can extract equipment/instruments from the process description using a Natural Language Processing library. This allows us to detect equipment in the process description and understand the interrelations.

## Storing Information as a Graph
We use [Neo4j](http://neo4j.com/) as a graph database to store the relational information.

We can connect to Neo4j using the `py2neo` Python library.

To install `py2neo`, run:
```sh
pip install py2neo
```

This repo contains an initialization script [(`src/initialize-neo4j.py`)](src/initialize-neo4j.py) which connects to a local instance of Neo4j and adds equipment; instruments; relations between them (`FLOWS_TO` and `MEASURES`).

Neo4j connection configuration can be changed in `src/config.py`.

## Evaluate Different Implementations and Choose Best One
This will involve enumerating through different position values such that the generated P&ID complies with the required standards, and is as efficient as possible.

## Create a DEXPI File
[DEXPI (Data Exchange in the Process Industry)](https://dexpi.org/) is an open standard for data exchange, based on XML, allowing for interoperability between vendors.

Based on the data obtained in the previous steps, we can use the `xml` Python library to create an XML file, in accordance with the DEXPI standard.

## Rule-Based Validation of P&IDs
We can define rules using a Cypher statement and query the Neo4j database to ensure that the P&ID is compliant.

An example of this can be seen in [`src/rule-based-validation.py`](src/rule-based-validation.py).

## License
The content of the README is distributed under the [CC0 1.0 Universal license](https://creativecommons.org/publicdomain/zero/1.0/). The code in Text to P&ID is distributed under the [MIT license](LICENSE).

---

We at [PlantFCE](https://plantfce.com/) are creating a pipeline that enables us to go from process description to P&ID.

> Annotate and digitize your P&IDs with PlantFCE eAI. [Learn more →](https://tryeai.com/)