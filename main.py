import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"
contents = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
response = client.models.generate_content(model=model, contents=messages)

if args.verbose:
    print("User prompt:", contents)

    if response.usage_metadata:
        prompt_token = response.usage_metadata.prompt_token_count
        response_token = response.usage_metadata.candidates_token_count

        print(f"Prompt tokens: {prompt_token}")
        print(f"Response tokens: {response_token}")
    else:
        raise RuntimeError("Usage metadata not found")

print("Response:")
print(response.text)