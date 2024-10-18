# WARNING: This example contains hard-coded secrets. Do not use in production!

API_KEY = "aoprtnfdfdgjdf-12121ng"
DATABASE_PASSWORD = "your@password"

def connect_to_database(password):
    if password == DATABASE_PASSWORD:
        print("Connected to the database.")
    else:
        print("Failed to connect to the database.")

def make_api_call(api_key):
    if api_key == API_KEY:
        print("API call successful.")
    else:
        print("Invalid API key.")

if __name__ == "__main__":
    connect_to_database("your_password_here")
    make_api_call("your_api_key_here")
