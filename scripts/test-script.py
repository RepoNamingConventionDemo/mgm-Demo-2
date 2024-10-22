# secrets_test.py
import os

# Intentionally exposing a secret API key
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Example secret key

def connect_to_service():
    print(f"Connecting with API Key: {API_KEY}")

if __name__ == "__main__":
    connect_to_service()
