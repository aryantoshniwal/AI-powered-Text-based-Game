import os
from dotenv import load_dotenv, find_dotenv

# These expect to find a .env file at the directory above the lesson. 
# The format for that file is: API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService

def load_env():
    _ = load_dotenv(find_dotenv())  # Load environment variables if needed

def get_together_api_key():
    # Return your hardcoded API key
    together_api_key = "write your api key here"
    return together_api_key
