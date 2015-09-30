from PIL import Image
import PIL.ImageOps

def fileToBinary():
	file = open("Secret.txt", "rb")
	readFile = bytearray(file.read())
	for bits in readFile:
		print bits
	#convert = "".join(format(x, 'b').zfill(8) for x in bytearray(readFile))

def stringToBinary():
	message = raw_input("Type the message to be hidden: ")
	convert = "".join(format(x, 'b').zfill(8) for x in bytearray(message))
	print convert

def coverImage():

	#Open image
	coverImage = Image.open("trollface.bmp")
	#convert the image into RGBA
	rgba_img = coverImage.convert('RGBA')
	#grab the size of image and store it into width and height
	width, height = coverImage.size

	for x in range(width):
		for y in range(height):
			r, g, b, a = rgba_img.getpixel((x, y))
			red = list(bin(r)[2:].zfill(8))
			green = bin(g)[2:].zfill(8)
			blue = bin(b)[2:].zfill(8)
			alpha = bin(a)[2:].zfill(8)
			print red
			print green
			print blue
			print alpha

fileToBinary()
#coverImage()