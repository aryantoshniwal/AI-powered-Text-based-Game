import os
from dotenv import load_dotenv, find_dotenv
import json
from together import Together

# these expect to find a .env file at the directory above the lesson.
# The format for that file is (without the comment): API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService

def load_env():
    _ = load_dotenv(find_dotenv())  # Load the environment variables if needed

def load_world(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_world(world, filename):
    with open(filename, 'w') as f:
        json.dump(world, f)

def get_together_api_key():
    # Manually set the API key here
    together_api_key = "dcf499b20ea0bb648c1e66679cee413138ec35748693ff6d42059c3e45292bbe"  # Replace with your actual API key
    return together_api_key
