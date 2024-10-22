# secrets_test_3.py
import os

# Intentionally exposing a secret stored in an environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://user:password@localhost/db")  # Example URL

def connect_to_database():
    print(f"Connecting to database at: {DATABASE_URL}")

if __name__ == "__main__":
    connect_to_database()
