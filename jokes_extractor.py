import re

def extract_jokes(response):
    pattern = r"Why did the (.+?) \? Because(.+)"
    matches = re.findall(pattern, response)
    jokes = [(setup, punchline) for setup, punchline in matches]
    return jokes

