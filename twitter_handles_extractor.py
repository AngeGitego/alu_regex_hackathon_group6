import re

def extract_twitter_handles(response):
    pattern = r"@(\w+)"
    twitter_handles = re.findall(pattern, response)
    return twitter_handles

