#!usr/bin/env/python3
from PIL import Image
import os

# img = Image.open("BRUM.jpg") # getting image object
# img.show() # opening
# img.save("BRUM.png") # saving to other format

# looping through all images and saving it to png format
for f in os.listdir('.'):
	if f.endswith('.jpg'):
		img = Image.open(f)
		filename, file_extension = os.path.splitext(f)
		img.save("PNG/{}.png".format(filename)) # this save to PNG folder

#RESIZING IMAGE/MUTIPLE RESIZING AT TIME
IMAGE_SIZE = (300, 300)
IMAGE_SIZE_2 = (700, 700)
for f in os.listdir('.'):
	if f.endswith('.jpg'):
		img = Image.open(f)
		filename, file_extension = os.path.splitext(f)

		img.thumbnail(IMAGE_SIZE)
		img.save("300/{}_300{}".format(filename, file_extension)) # this save to PNG folder

		img.thumbnail(IMAGE_SIZE_2)
		img.save("700/{}_300{}".format(filename, file_extension)) # this save to PNG folder



# print(dir(os))
# print(os.getlogin()) # user
