// 1. Wipe the database to start fresh
MATCH (n) DETACH DELETE n;

// 2. Create the Uniqueness Constraint (Crucial for preventing duplicates)
CREATE CONSTRAINT attendee_unique_id IF NOT EXISTS
FOR (a:Attendee) REQUIRE a.AttendeeID IS UNIQUE;

// 3. Create Attendees using MERGE (Safe for re-running)
MERGE (:Attendee {AttendeeID: 101});
MERGE (:Attendee {AttendeeID: 102});
MERGE (:Attendee {AttendeeID: 103});
MERGE (:Attendee {AttendeeID: 104});
MERGE (:Attendee {AttendeeID: 105});
MERGE (:Attendee {AttendeeID: 106});
MERGE (:Attendee {AttendeeID: 107});
MERGE (:Attendee {AttendeeID: 108});
MERGE (:Attendee {AttendeeID: 109});
MERGE (:Attendee {AttendeeID: 110});
MERGE (:Attendee {AttendeeID: 111});
MERGE (:Attendee {AttendeeID: 113});
MERGE (:Attendee {AttendeeID: 114});
MERGE (:Attendee {AttendeeID: 115});
MERGE (:Attendee {AttendeeID: 116});
MERGE (:Attendee {AttendeeID: 117});
MERGE (:Attendee {AttendeeID: 118});
MERGE (:Attendee {AttendeeID: 120});

// 4. Create Relationships (Using MERGE to avoid duplicate lines)
MATCH (a:Attendee {AttendeeID: 101}), (b:Attendee {AttendeeID: 109}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 101}), (b:Attendee {AttendeeID: 107}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 102}), (b:Attendee {AttendeeID: 110}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 103}), (b:Attendee {AttendeeID: 111}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 104}), (b:Attendee {AttendeeID: 120}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 105}), (b:Attendee {AttendeeID: 113}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 106}), (b:Attendee {AttendeeID: 114}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 107}), (b:Attendee {AttendeeID: 115}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 108}), (b:Attendee {AttendeeID: 116}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 111}), (b:Attendee {AttendeeID: 101}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 106}), (b:Attendee {AttendeeID: 103}) MERGE (a)-[:CONNECTED_TO]->(b);
MATCH (a:Attendee {AttendeeID: 120}), (b:Attendee {AttendeeID: 103}) MERGE (a)-[:CONNECTED_TO]->(b);