from neo4j import GraphDatabase


driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver= GraphDatabase.driver(uri, auth=("neo4j", "neo4j1234"),max_connection_lifetime =1000)

def get_connection(tx,id):
    query ="MATCH (a:Attendee {AttendeeID:$find})-[r:CONNECTED_TO]-(b:Attendee) RETURN b.AttendeeID AS ConnectedID"
    results= tx.run(query,find = id)
    connections =[]
    for result in results:
        connections.append(result["ConnectedID"])
    return connections

def add_connection_tx(tx, id1, id2):
    val1 = int(id1)
    val2 = int(id2)
    check_query = """
    MATCH (a:Attendee {AttendeeID: $id1})-[r:CONNECTED_TO]-(b:Attendee {AttendeeID: $id2})
    RETURN r
    """
    result = tx.run(check_query, id1=val1, id2=val2)
    if result.peek():
        return False
    create_query = """
    MERGE (a:Attendee {AttendeeID: $id1})
    MERGE (b:Attendee {AttendeeID: $id2})
    WITH a, b
    WHERE NOT (a)-[:CONNECTED_TO]-(b)
    CREATE (a)-[:CONNECTED_TO]->(b)
    """
    tx.run(create_query, id1=val1, id2=val2)
    return True
        
def create_connections(id1,id2):
    connect()
    with driver.session() as session:
        return session.execute_write(add_connection_tx, id1, id2)
    