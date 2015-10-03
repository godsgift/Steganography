from PIL import Image
import PIL.ImageOps
import sys
import array
import binascii

def pixyGrabber():
	global secretMessageSizeAscii
	global rgb_array
	global tat
	rgb_array = ""
	secretImage = Image.open("test.bmp")
	rgb_img = secretImage.convert('RGB')
	width, height = rgb_img.size
	rgb_array_list = []

	nullCondition = "00000000"
	group = ""
	secretMessageSize = ""
	secretMessageIndex = 0
	nullCounter = 1
	temp = ""
	binStringSecretMsg = ""
	secretMessageSizeAscii = ""
	tet = 0
	cCounter = 0
	tat = ""
	#iterate through all the pixels
	for x in range(width):
		for y in range(height):
			#go through each pixel grabbing string of 0's and 1's
			r, g, b = rgb_img.getpixel((x, y))
			redBinString = str(bin(r)[2:].zfill(8))[7]
			greenBinString = str(bin(g)[2:].zfill(8))[7]
			blueBinString = str(bin(b)[2:].zfill(8))[7]

			rgb_array += redBinString + greenBinString + blueBinString
	
	#group the string in chunks of 8 so that its in binary
	group = [rgb_array[i:i +8] for i in range(0, len(rgb_array), 8)]

	for i in group:

		temp += i
		if (i == nullCondition and nullCounter == 1):
			fileName_bytes = temp[0:len(temp) - 8]
			#print fileName_bytes
			nullCounter += 1
			temp = ""
		elif (i == nullCondition and nullCounter == 2):
			secretMessageSize = temp[0:len(temp) - 8]
			secretMessageSizeList = list(secretMessageSize)
			counter = 0
			for j in range(len(secretMessageSizeList)/8):
				for i in range(0, 8):
					binStringSecretMsg += secretMessageSizeList[counter]
					counter += 1
				secretMessageSizeAscii += ''.join(chr(int(binStringSecretMsg[i:i+8], 2)) for i in xrange(0, len(binStringSecretMsg), 8))
				binStringSecretMsg = ""
			tet =  int(secretMessageSizeAscii)
			print tet
			nullCounter += 1

		elif(nullCounter == 3):
			for k in range(tet):
				tat += group[cCounter+k]
			return
			nullCounter += 1
		cCounter += 1
			

def newFile():
	secretData = ""
	byteAray = []

	#iterate through the size of the secret message and add the last bits into secretData
	for i in range(int(secretMessageSizeAscii)):
		secretData += tat[i]

	newByteArray = []
	#
	for i in range (0, len(secretData)/8):
		newByteArray.append(int(secretData[i*8:(i+1) * 8], 2))

	byteArray = array.array('B', newByteArray).tostring()
	secretMessage = bytearray(byteArray)

	createFile = open('test.txt', 'w')
	createFile.write(secretMessage)

if __name__ == "__main__":
	pixyGrabber()
	newFile()