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

def compare(hiddenFile, coverFile):
	coverImageSize = os.path.getsize(coverFile)
	print "Your cover image size is: %d" %coverImageSize
	hiddenFileSize = os.path.getsize(hiddenFile)
	print "Your hidden image size is: %d" %hiddenFileSize

def stego():
	#Open image
	coverImage = Image.open("trollface2.bmp")
	#convert the image into RGBA
	rgb_img = coverImage.convert('RGB')
	#grab the size of image and store it into width and height
	width, height = coverImage.size
	#grab the file to be hidden from secretFile method
	secret = secretFile()
	dataCounter = 0
	for x in range(width):
		for y in range(height):
			#grab the rgba value of each pixel
			r, g, b = rgb_img.getpixel((x, y))
			#convert each rgba value into binary
			red = list(bin(r)[2:].zfill(8))
			green = list(bin(g)[2:].zfill(8))
			blue = list(bin(b)[2:].zfill(8))
			#put each pixels rgba into an array
			rgb_array = [red, green, blue]
			# #grab each pixels rgb
			for epix in rgb_array:
				if dataCounter + 1 <= len(secret):
					#replace the last bit to the hidden data's bit
					epix[7] = secret[dataCounter]
					dataCounter += 1
					red = "".join(epix)
					green = "".join(epix)
					blue = "".join(epix)
					print dataCounter
					print red
					print green
					print blue
				
if __name__ == "__main__":	
	secretFile()
	stego()
	#compare("trollface.bmp", "Secret.txt")