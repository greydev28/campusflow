# CampusFlow — IT Support Ticket Manager

CampusFlow is a beginner-friendly Python command-line application for managing IT support requests.
It helps staff record, track, search, assign, and close support tickets.

## Features
- Automatically generates unique ticket IDs (e.g., `T001`, `T002`).
- Creates tickets for Network, Hardware, Software, and Other issues.
- Calculates ticket priority based on urgency and affected users.
- Views and searches existing tickets.
- Assigns tickets to support staff.
- Closes resolved tickets.
- Saves and loads ticket records using JSON.
- Includes automated tests using Python's `unittest` module.

## Technologies
- Python
- JSON
- `unittest`

## How to Run
1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the application:

   ```bash
   python main.py
   ```

4. Run the automated tests:

   ```bash
   python -m unittest -v test_campusflow.py
   ```

## Purpose
This project demonstrates practical Python programming concepts, including classes, objects, 
functions, lists, file handling, JSON, exception handling, and automated testing.
