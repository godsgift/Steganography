#############################################################################
#Created by: Elton Sia A00800541
#
#File: stegosaurus.py
#
#This program hides secret data inside a cover image. Data can be an image or 
#a text file. The secret data gets hidden inside a cover image using LSB 
#method. The user may specifiy which secret data and cover image they wish
#to use as well as the name of the output file.
#Note: the output file must be in bmp format
#Before the encoding starts, the progam checks first if the secret data size 
#can be stuffed into the cover image, if not, the encoding does not start
#
#Functions:
#usage():
#secretFile():
#compare():
#stegosaurus():
#main
#
#############################################################################

from PIL import Image
import PIL.ImageOps
import os
import sys

def usage():
    if len(sys.argv) !=  4:
        print "To use: ", sys.argv[0], "CoverImage FileToHide OutputFileName"
        sys.exit()

def secretFile():
	bits = ""
	lbits = []
	fileNameBin =""
	fileName = str(sys.argv[2])
	secretData = str(sys.argv[2])
	totalDataSize = ""

	for x in bytearray(fileName):
		fileNameBin += bin(x)[2:].zfill(8)
	fileNameBin += "00000000"

	#open file as read and binary mode
	file = open(secretData, "rb")
	#convert whatever is in the file into bytes
	readFile = bytearray(file.read())

	#convert the bytes into bits
	for bit in readFile:
		#store all the bits into a string
		bits += bin(bit)[2:].zfill(8)
	#change the datasize from an int to binary and put into a list so we can send it
	listDataSize = list(str(len(bits)))
	totalDataSize = "".join(format(x, 'b').zfill(8) for x in bytearray(listDataSize))
	
	totalDataSize += "00000000"
	lbits += list(fileNameBin) + list(totalDataSize) + list(bits)
	return lbits

def compare():
	coverImage = Image.open(str(sys.argv[1]))
	width, height = coverImage.size
	bitsCanStore = width*height*3

	secret = []
	secret = secretFile()
	totalBits = len(secret)
	if totalBits <= bitsCanStore:
		stegosaurus()
	else:
		print ("The file you want to hide is too large. Please choose a smaller file size")

def stegosaurus():
	coverImage = Image.open(str(sys.argv[1]))
	#convert the image into RGBA
	rgb_img = coverImage.convert('RGB')
	#grab the size of image and store it into width and height
	width, height = rgb_img.size
	#grab the data we want to hide from the secretFile method and store it in a list
	secret = []
	secret = secretFile()
	#Find out how many bits we will be storing into the cover image
	totalBits = len(secret)
	bit_index = 0
	rgb_array = []
	outPutFileName = str(sys.argv[3])

	testRed =[]
	#iterate through all the pixels
	for x in range(width):
		for y in range(height):
			r, g, b = rgb_img.getpixel((x, y))
			#convert to binary and then put into a list
			redBin = list(bin(r)[2:].zfill(8))
			greenBin = list(bin(g)[2:].zfill(8))
			blueBin = list(bin(b)[2:].zfill(8))
			#put the list of rgb into a list 

			rgb_array = [redBin, greenBin, blueBin]
			rgb_decimal = []

			redDecimal = r
			greenDecimal = g
			blueDecimal = b

			#we can only loop through 3 times because of RGB
			for i in range(3):
				#Use the original green or blue when creating the image if when storing the last bit stops at red or green.
				if (bit_index >= (totalBits - 1)):
					rgb_img.putpixel((x, y), (redDecimal, greenDecimal, blueDecimal))
					rgb_img.save(outPutFileName)
					return

				#swap the last bit of each rgb
				rgb_array[(i)][7] = secret[bit_index]
				rgb_array[(i)] = rgb_array[(i)]
				#print redDecimal
				bit_index += 1

				#join the new last bit to the rest of the bits for each colour (RGB)
				if (i == 0):
					tempRed = "".join(rgb_array[i])
					redDecimal = int(tempRed, 2)
				elif (i == 1):
					tempGreen = "".join(rgb_array[i])
					greenDecimal = int(tempGreen, 2)
				else:
					tempBlue = "".join(rgb_array[i])
					blueDecimal = int(tempBlue, 2)
				#create the new image with the modified RGB
				rgb_img.putpixel((x,y), (redDecimal, greenDecimal, blueDecimal))
	#save the image if it loops perfectly
	#ie if it stores the last bit in blue
	rgb_img.save(outPutFileName)
				
if __name__ == "__main__":	
	usage()
	secretFile()
	compare()
