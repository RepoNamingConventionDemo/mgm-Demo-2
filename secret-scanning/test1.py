# test_secrets.py

# Mock secret values for testing
API_KEY = "12345-abcde-67890-fghij"
GITHUB_TOKEN = "ghp_abc123def456ghi789jkl"
DATABASE_URL = "postgres://user:pass@localhost:5432/dbname"
AWS_ACCESS_KEY_ID = "AKIAEXAMPLE12345"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
SENDGRID_API_KEY = "SG.abc123xyz456@example.com"
PAYPAL_CLIENT_SECRET = "EKu37zYdKpLejksdkjfhjk37Zsdjk"
TWILIO_AUTH_TOKEN = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SECRET_KEY = "supersecretkey123"
JWT_SECRET = "jwt-secret-987654321"
OAUTH2_CLIENT_SECRET = "client-secret-abcdefg"

def connect_to_api(api_key):
    print(f"Connecting to API with API Key: {api_key}")

def connect_to_database(db_url):
    print(f"Connecting to Database at: {db_url}")

def process_payment(secret_key):
    print(f"Processing payment with secret key: {secret_key}")

def send_email(api_key):
    print(f"Sending email using API key: {api_key}")

def main():
    print("Testing secret scanning alerts...")

    # Simulate API connection
    connect_to_api(API_KEY)
    
    # Simulate Database connection
    connect_to_database(DATABASE_URL)
    
    # Simulate payment processing
    process_payment(STRIPE_SECRET_KEY)
    
    # Simulate email sending
    send_email(SENDGRID_API_KEY)
    
    # Additional mock functions
    print("Using GitHub token:", GITHUB_TOKEN)
    print("Using AWS access key:", AWS_ACCESS_KEY_ID)
    print("Using AWS secret access key:", AWS_SECRET_ACCESS_KEY)
    print("Using PayPal client secret:", PAYPAL_CLIENT_SECRET)
    print("Using Twilio auth token:", TWILIO_AUTH_TOKEN)
    print("Using JWT secret:", JWT_SECRET)
    print("Using OAuth2 client secret:", OAUTH2_CLIENT_SECRET)

if __name__ == "__main__":
    main()
