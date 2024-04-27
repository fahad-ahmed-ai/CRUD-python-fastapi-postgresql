# FastAPI Project

This is a FastAPI project for managing user transactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fahad-ahmed-ai/CRUD-python-fastapi-postgresql.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

## API Endpoints

- `/login` (POST): User login.
- `/register` (POST): User registration.
- `/transactions` (POST): Create a new transaction.
- `/get_transactions` (GET): Get all transactions for the authenticated user.
- `/transactions/{transaction_id}` (PUT): Update a transaction.
- `/transactions/{transaction_id}` (DELETE): Delete a transaction.

## Project Structure

- `main.py`: FastAPI app setup and initialization.
- `database.py`: Database configuration and session management.
- `models.py`: SQLAlchemy models for user and transaction.
- `schemas.py`: Pydantic models for request and response schemas.
- `views.py`: API endpoints and request handling logic.

## Environment Variables

- `DB_USER`: Database username.
- `DB_PASSWORD`: Database password.
- `DB_HOST`: Database host address.
- `DB_PORT`: Database port.
- `DB_NAME`: Database name.

Make sure to set these environment variables before running the application.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
