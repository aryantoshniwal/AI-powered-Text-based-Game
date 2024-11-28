import os
from dotenv import load_dotenv, find_dotenv

# These expect to find a .env file at the directory above the lesson. 
# The format for that file is: API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService

def load_env():
    _ = load_dotenv(find_dotenv())  # Load environment variables if needed

def get_together_api_key():
    # Return your hardcoded API key
    together_api_key = "dcf499b20ea0bb648c1e66679cee413138ec35748693ff6d42059c3e45292bbe"
    return together_api_key
