# Work List Manager

A simple CLI (Command Line Interface) application built with Python to manage your daily tasks, work list, or goals. It uses SQLite for permanent data storage and PrettyTable for interactive, clean terminal formatting.

## Features

- **Add Tasks**: Easily save new tasks with a title and a description.
- **View Options**: Read all tasks at once or look up a specific task by its ID or Title.
- **Modify Tasks**: Update task details dynamically using either their ID or Title.
- **Delete Tasks**: Remove completed or unwanted tasks from the database by ID or Title.
- **Persistent Storage**: Data is automatically saved inside a local SQLite database (`data/menager.db`).

## Prerequisites

Make sure you have Python 3.x installed on your machine. 

This application relies on the `prettytable` library to display menus and errors. You can install it via pip:

```bash
pip install prettytable
```

## How to Run

1. Clone or download this repository.
2. Open your terminal or command prompt in the project directory.
3. Run the script using the following command:

```bash
python main.py
```
*(Replace `main.py` with the actual name of your script file if it is named differently).*

## Database Structure

On the very first launch, the script automatically creates a `data/` folder and establishes a database file named `menager.db` inside it. 

The structure of the `Work_List` table is as follows:
- `Id`: Integer (Primary Key, Auto-increment)
- `Title`: Text (Name of the task)
- `Work`: Text (Detailed explanation of the task)

## Navigation Menu

When running the application, you will interact with the following CLI choices:
1. **Add work** — Create a new task entry.
2. **Change work** — Edit existing tasks (Look up by ID or Title).
3. **Open all works** — Print all tasks stored in the database.
4. **Open one work** — View a specific task details.
5. **Delete work** — Erase a task from the list.
6. **Exit** — Safely close the database connection and close the app.