import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

# api_key check
if isinstance(api_key, None):
    raise RuntimeError("api_key is none")

## creating client ##
client = OpenAI(
    base_url = "https://openrouter.ai/api/v1"
    api_key = api_key
)