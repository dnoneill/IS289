'''base class and sub class, understand inheritance and unit tests that
test methods.

travis to github, create repo.

send link to repo.'''
import unittest

class AudioVisual():
	def __init__(self, title, mediatype, genre):
		self.title = title
		self.mediatype = mediatype
		self.genre = genre
	def report(self):
		return 'Title: {}\nMedia Type: {}\nGenre: {}'.format(self.title, self.mediatype, self.genre)

class TVShow(AudioVisual):
	def __init__(self, title, mediatype, genre, seasons, epruntime, rating):
		super().__init__(title, mediatype, genre)
		self.seasons = seasons
		self.epruntime = epruntime
		self.rating = rating
	def report(self):
		return super().report() + "\nNumber of Seasons: {}\nEpisode Length: {}\nRating: {}".format(self.seasons, self.epruntime, self.rating)

class Movie(AudioVisual):
	def __init__(self, title, mediatype, genre, runtime, sequels, rating):
		super().__init__(title, mediatype, genre)
		self.runtime =  runtime
		self.sequels = sequels
		self.rating = rating
	def report(self):
		return super().report() + "\nRuntime: {}\nSequels: {}\nRating: {}".format(self.runtime, self.sequels, self.rating)

class Music(AudioVisual):
	def __init__(self, title, mediatype, genre, length, artist, numbalbums):		
		super().__init__(title, mediatype, genre)
		self.length = length
		self.artist = artist
		self.numbalbums = numbalbums
	def report(self):
		return super().report() + "\nAlbum Length: {}\nArtist: {}\nNumber of Albums by {}: {}".format(self.length, self.artist, self.artist, self.numbalbums)

class UnitTest(unittest.TestCase):
	def test_audiovisual(self):
		result = Movie("The Princess Bride", "DVD", "Fantasy", "98 min", "", "PG").report()
		self.assertEqual(result, "Title: The Princess Bride\nMedia Type: DVD\nGenre: Fantasy\nRuntime: 98 min\nSequels: \nRating: PG")
		
		result = TVShow("Parks and Recreation", "Netflix", "Comedy", "7", "42 min", "PG").report()
		self.assertEqual(result, "Title: Parks and Recreation\nMedia Type: Netflix\nGenre: Comedy\nNumber of Seasons: 7\nEpisode Length: 42 min\nRating: PG")

if __name__ == "__main__":
	unittest.main()