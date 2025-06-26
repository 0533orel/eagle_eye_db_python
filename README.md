
# Eagle Eye DB

Eagle Eye DB is a lightweight command‑line tool written in Python for managing a small agent registry.  
It demonstrates a clean separation between domain models, a data access layer (DAL) and a CLI application layer while persisting data in a MySQL database.

## Features

* Create, read, update and delete (CRUD) records in the `agents` table.
* Increment mission‑completion counters for individual agents.
* Input validation loops that prevent incorrect data entry.
* Modular architecture (`models`, `dal`, `validation`, `main.py`) enabling easy testing and extension.

## Project Structure

```text
eagle_eye_db/
├── dal/
│   ├── agent_dal.py         # CRUD operations and SQL queries
│   └── db_connection.py     # MySQL connection helper
├── models/
│   └── agent.py             # Domain object representing an agent
├── create_eagleEyeDB.sql    # Script that creates the database and table
├── main.py                  # Command‑line interface
├── validation.py            # Console‑input validation utilities
└── requirements.txt         # Python dependencies
```

## Prerequisites

* Python 3.9 or later  
* MySQL Server 8.x  
* A MySQL user account with permission to create databases and tables

## Installation

```bash
# Clone the repository
git clone https://github.com/<your‑organisation>/eagle_eye_db.git
cd eagle_eye_db

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate    # On Windows use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Database Setup

1. Ensure the MySQL server is running.  
2. Edit `dal/db_connection.py` if necessary to reflect your MySQL credentials.  
3. Execute the SQL script:

```bash
mysql -u <user> -p < create_eagleEyeDB.sql
```

The command creates the database `eagleEyeDB` and its `agents` table.

## Running the Application

```bash
python main.py
```

You will be presented with an interactive menu:

```
===== EAGLE EYE ‑ AGENT CONTROL MENU =====
1. View all agents
2. Add new agent
3. Update agent
4. Delete agent
5. Exit
```

Follow the on‑screen prompts to manage agent records.

## Configuration

Connection parameters are defined in `dal/db_connection.py`:

```python
self.conn_str = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": db_name
}
```

Adjust the values to match your environment.

## Extending the Project

* **Unit tests** – Add tests in a `tests/` folder and inject mock connections.  
* **Logging** – Replace `print` statements with the `logging` module.  
* **Context managers** – Refactor database transactions to use `with` blocks for automatic cleanup.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
