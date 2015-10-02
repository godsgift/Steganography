from PIL import Image
import PIL.ImageOps
import os

def secretFile():
	bits = ""
	lbits = []
	#open file as read and binary mode
	file = open("Secret.txt", "rb")
	#convert whatever is in the file into bytes
	readFile = bytearray(file.read())
	#convert the bytes into bits
	for bit in readFile:
		#store all the bits into a string
		bits += bin(bit)[2:].zfill(8)
	lbits = list(bits)
	#print lbits
	return lbits
	#convert = "".join(format(x, 'b').zfill(8) for x in bytearray(readFile))

def compare():
	coverImage = Image.open("trollface.bmp")
	width, height = coverImage.size
	bitsCanStore = width*height*3

	secret = []
	secret = secretFile()
	totalBits = len(secret)

	if totalBits <= bitsCanStore:
		stego()


def stego():
	coverImage = Image.open("trollface.bmp")
	#convert the image into RGBA
	rgb_img = coverImage.convert('RGB')
	#grab the size of image and store it into width and height
	width, height = rgb_img.size
	secret = []
	secret = secretFile()
	totalBits = len(secret)
	bit_index = 0
	rgb_array = []

	for x in range(width):
		for y in range(height):
			r, g, b = rgb_img.getpixel((x, y))
			#convert to binary and then put into a list
			redBin = list(bin(r)[2:].zfill(8))
			greenBin = list(bin(g)[2:].zfill(8))
			blueBin = list(bin(b)[2:].zfill(8))
			#put the list of rgb into a list 
			rgb_array.append(redBin)
			rgb_array.append(greenBin)
			rgb_array.append(blueBin)

			redDecimal = r
			greenDecimal = g
			blueDecimal = b

			for i in range(3):
				if (bit_index >= (totalBits - 1)):
					rgb_img.putpixel((x, y), (redDecimal, greenDecimal, blueDecimal))
					rgb_img.save("test.bmp")
					return

				rgb_array[(i)][7] = secret[bit_index]
				rgb_array[(i)] = rgb_array[(i)]
				bit_index += 1

				if (i == 0):
					tempRed = "".join(rgb_array[i])
					redDecimal = int(tempRed, 2)
				elif (i == 1):
					tempGreen = "".join(rgb_array[i])
					greenDecimal = int(tempGreen, 2)
				else:
					tempBlue = "".join(rgb_array[i])
					blueDecimal = int(tempBlue, 2)

			rgb_img.putpixel((x,y), (redDecimal, greenDecimal, blueDecimal))

	rgb_img.save("test.bmp")
				
if __name__ == "__main__":	
	#secretFile()
	#stego()
	compare()
	#decode()