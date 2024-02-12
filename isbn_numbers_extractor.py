import re

def extract_isbn_numbers(response):
    pattern = r"ISBN (\d{3}-\d-\d{3}-\d{5}-\d)"
    matches = re.findall(pattern, response)
    isbn_numbers = matches
    return isbn_numbers

