# Conference Management System
**University Module:** [8637 -- APPLIED DATABASES]  
**Academic Year:** 2025/2026  
**Student Name:** [Andre Hoarau]  
**Student ID:** [G00439332]
**Contact:** G00439332@atu.ie

---

## 1. Project Overview
This application is a dual-database management system designed to handle conference logistics and social networking. It utilizes an **N-Tier Architecture** to separate user interaction, business logic, and data access.

The system integrates:
*   **Relational Database (MySQL):** Handles structured data such as Attendees, Rooms, Sessions, and Companies.
*   **Graph Database (Neo4j):** Manages the social graph, allowing attendees to form professional connections and discover networking paths.

---

## 2. VM Environment Setup
To run this application on the Virtual Machine, please follow these steps to ensure all dependencies and services are correctly configured.

### Prerequisites
*   **Python 3.x**
*   **MySQL Server** (Service running on port 3306)
*   **Neo4j** (Service running on port 7687)

### Installation
1.  **Extract the project files** to your directory of choice.
2.  **Install Python Packages:** Open a terminal in the project folder and run:
    ```bash
    pip install -r requirements.txt