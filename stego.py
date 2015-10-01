from PIL import Image
import PIL.ImageOps
import os

def secretFile():
	bits = ""
	#open file as read and binary mode
	file = open("Secret.txt", "rb")
	#convert whatever is in the file into bytes
	readFile = bytearray(file.read())
	#convert the bytes into bits
	for bit in readFile:
		#store all the bits into a string
		bits += bin(bit)[2:].zfill(8)
	lbits = list(bits)
	return lbits
	#convert = "".join(format(x, 'b').zfill(8) for x in bytearray(readFile))

def stringToBinary():
	message = raw_input("Type the message to be hidden: ")
	convert = "".join(format(x, 'b').zfill(8) for x in bytearray(message))
	print convert

def compare(hiddenFile, coverFile):
	coverImageSize = os.path.getsize(coverFile)
	print "Your cover image size is: %d" %coverImageSize
	hiddenFileSize = os.path.getsize(hiddenFile)
	print "Your hidden image size is: %d" %hiddenFileSize

def stego():
	#Open image
	coverImage = Image.open("trollface2.bmp")
	#convert the image into RGBA
	rgba_img = coverImage.convert('RGBA')
	#grab the size of image and store it into width and height
	width, height = coverImage.size

	secret = secretFile)

	#imgSize = width*height
	#print imgSize
	for x in range(width):
		for y in range(height):
			#grab the rgba value of each pixel
			r, g, b, a = rgba_img.getpixel((x, y))
			#convert each rgba value into binary
			red = list(bin(r)[2:].zfill(8))
			green = list(bin(g)[2:].zfill(8))
			blue = list(bin(b)[2:].zfill(8))
			alpha = list(bin(a)[2:].zfill(8))
			#put each pixels rgba into an array
			rgba_array = [red, green, blue, alpha]
			#grab each pixels rgba
			for epix in rgba_array:
				#print epix[7]
				return

if __name__ == "__main__":	
	secretFile()
	stego()
	#compare("trollface.bmp", "Secret.txt")