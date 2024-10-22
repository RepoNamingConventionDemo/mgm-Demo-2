# secrets_test_2.py
# Intentionally exposing a secret token
SECRET_TOKEN = "s3cr3t_t0k3n_12345"  # Example token

def access_secure_resource():
    print(f"Accessing resource with token: {SECRET_TOKEN}")

if __name__ == "__main__":
    access_secure_resource()
