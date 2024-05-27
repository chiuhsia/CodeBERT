import os

# Fetch the environment variable
secret_value = os.getenv('MY_SECRET')

if secret_value:
    print(f"Secret is configured correctly: {secret_value}")
else:
    print("Secret is not configured correctly.")

