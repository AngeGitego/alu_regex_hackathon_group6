import re

def extract_movie_titles(response):
    pattern = r"([A-Za-z\s]+) \((\d{4})\)"
    matches = re.findall(pattern, response)
    movie_titles = [(title, year) for title, year in matches]
    return movie_titles

