import re

def extract_song_lyrics(response):
    pattern = r"\[Verse (\d+)\] (.+)"
    matches = re.findall(pattern, response)
    song_lyrics = [(verse_number, lyrics) for verse_number, lyrics in matches]
    return song_lyrics

