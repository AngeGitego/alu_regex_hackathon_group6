from movie_titles_extractor import extract_movie_titles
from song_lyrics_extractor import extract_song_lyrics
from twitter_handles_extractor import extract_twitter_handles
from isbn_numbers_extractor import extract_isbn_numbers
from jokes_extractor import extract_jokes

# Sample string responses
movie_response = "The Shawshank Redemption (1994), Titanic (1997)"
song_response = "[Verse 1] This is the song lyrics... [Verse 2] More lyrics..."
twitter_response = "Follow me on Twitter @user1 and @user2"
isbn_response = "ISBN 123-4-567-89012-3, ISBN 456-7-890-12345-6"
jokes_response = "Why did the chicken cross the road? Because it wanted to get to the other side."

# Test movie titles extraction
print("Movie Titles:")
print(extract_movie_titles(movie_response))

# Test song lyrics extraction
print("\nSong Lyrics:")
print(extract_song_lyrics(song_response))

# Test Twitter handles extraction
print("\nTwitter Handles:")
print(extract_twitter_handles(twitter_response))

# Test ISBN numbers extraction
print("\nISBN Numbers:")
print(extract_isbn_numbers(isbn_response))

# Test jokes extraction
print("\nJokes:")
print(extract_jokes(jokes_response))
