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

def get_connections_list(id):
    connect()
    with driver.session() as session:
        return session.execute_read(get_connection, id)
        

    