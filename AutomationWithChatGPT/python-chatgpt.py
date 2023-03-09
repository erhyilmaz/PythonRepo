import requests
import argparse
import os

'''
Usage: $python3 python-chatgpt.py "task description for ChatGPT" "output_file.py"
'''

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of file to save the script")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"

# Way 1 :
# api_key = "YOUR_OPENAI_KEY"

# Way 2 :
# First need to run "export OPENAI_API_KEY = YOUR_OPENAI_KEY" on Linux terminal
api_key = os.getenv("OPENAI_API_KEY")

request_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_header, json=request_data)

if response.status_code == 200:
    # print(response.json())
    # print(response.json()["choices"][0]["text"])

    # Write OpenGPT API output into a local .py file given as input argument
    response_code = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_code)
else:
    print(f"Request failed with status code: {str(response.status_code)}")
    print(response.json())

