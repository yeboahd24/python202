#!usr/bin/env/python

#interface
class AudioFile:
	def __init__(self, filename):
		if not filename.endswith(self.ext): # polymorphism
			raise Exception("Invalid file format")
		self.filename = filename


class MP3File(AudioFile):
	ext = "mp3" # polymorphism

	def play(self):
 		print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
	ext = "wav"

	def play(self):
		print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
	ext = "ogg"

	def play(self):
		print("playing {} as ogg".format(self.filename))




ogg = OggFile("myfile.ogg")
ogg.play()
mp3 = MP3File("myfile.mp3")
mp3.play()
# not_an_mp3 = MP3File("myfile.ogg") #error
# not_an_mp3.play()

