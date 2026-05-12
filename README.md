# Conference Management System
**University Module:** 8637 -- APPLIED DATABASES  
**Academic Year:** 2025/2026  
**Student Name:** Andre Hoarau  
**Student ID:** G00439332  
**Contact:** G00439332@atu.ie

---

## 1. Project Overview
This application is a dual-database management system designed to handle conference logistics and social networking. It utilizes an **N-Tier Architecture** to separate user interaction (CLI), business logic, and data access layers.

The system integrates:
*   **Relational Database (MySQL):** Handles structured data such as Attendees, Rooms, Sessions, and Companies.
*   **Graph Database (Neo4j):** Manages the social graph, allowing attendees to form professional connections and discover networking paths.
### Project Structure
```
applied_db_final_project/
├── appdbproj.sql         # MySQL Database Dump
├── main.py               # Main Application Logic & CLI
├── myneo4jaccess.py      # Neo4j Data Access Object (DAO)
├── mysqldbaccess.py      # MySQL Data Access Object (DAO)
├── requirements.txt      # Python Dependencies
├── README.md             # Project Documentation
├── setup_neo4j.cypher    # Neo4j Initialization Script
├── GitLink.txt           # Link to Version Control
└── .gitignore            # Git exclusion rules
```
---

## 2. Environment Setup & Services

### MySQL Service
1. **Database:** Create a schema named `appdbproj`.
2. **Data Import:** Import the provided `appdbproj.sql` file into your MySQL instance to set up all tables and initial data.
3. **Python Config:** Credentials are set to `root` / `root` in `mysqldbaccess.py`.

### Neo4j Service
1. **Database:** Create a database named `attendeeNetwork`.
2. **Setup:** Run the provided Cypher script. Note that this script uses `MERGE` and `CONSTRAINTS` to ensure a clean data state.
3. **Python Config:** Credentials are set to `neo4j` / `neo4j1234` in `myneo4jaccess.py`. 
    *   *Note to Examiners:* If the VM Neo4j password differs, please update the `auth` parameter in the `connect()` function within `myneo4jaccess.py`.

---

## 3. Installation & Execution
1. **Extract Files:** Unzip the project files into a local directory.
2. **Install Requirements:** Run the following command to install the Neo4j and PyMySQL drivers:
   ```bash
   pip install -r requirements.txt

---

## 4. Key Logic & Caching
*   **Choice 5 (Networking):** The application uses the Neo4j Python Driver's `execute_write` transaction pattern. It ensures that relationships between attendees are unique by verifying existing connections before creation.
*   **Choice 6 (Rooms):** This feature implements a **static cache**. To meet the project requirements, room data is fetched from the MySQL database only upon the first request. This data is stored in a local variable for the duration of the session. Any rooms added to the MySQL database while the program is running will not appear until the application is restarted.

---

## 5. Technical Documentation & Referencing
The following official documentation was used to ensure standard-compliant implementation and robust error handling:

*   **[PyMySQL Documentation](https://pymysql.readthedocs.io/):** Utilized for managing relational connections and implementing `DictCursor` for readable data mapping.
*   **[Neo4j Python Driver Manual](https://neo4j.com/docs/python-manual/current/):** Followed for implementing secure transaction units and the Bolt protocol.
*   **[Cypher Query Language Reference](https://neo4j.com/docs/cypher-cheat-sheet/):** Consulted for graph data modeling and relationship constraints.
*   **[PEP 249 – Python Database API Specification](https://peps.python.org/pep-0249/):** Followed to ensure the Data Access Object (DAO) patterns are consistent across different database drivers.

---