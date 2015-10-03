from PIL import Image
import PIL.ImageOps
import sys
import array

def pixyGrabber():
	global secretMessageSize
	global rgb_array
	rgb_array = ""
	secretImage = Image.open("test.bmp")
	rgb_img = secretImage.convert('RGB')
	width, height = rgb_img.size

	secretMessageSize = 264
	secretMessageIndex = 0

	#iterate through all the pixels
	for x in range(width):
		for y in range(height):
			#if we see a null ternimator everything before that is the filename
			#if we see a 2nd null terminator, everything before that is data size
			if secretMessageIndex <= secretMessageSize:
				#grab the rgb values from the x and y values of the pixels
				r, g, b = rgb_img.getpixel((x, y))
				#change rgb into binary then grab the last bit and turn it into a string
				redBinString = str(bin(r)[2:].zfill(8))[7]
				greenBinString = str(bin(g)[2:].zfill(8))[7]
				blueBinString = str(bin(b)[2:].zfill(8))[7]
				#combine all the rgb string values and put it into rgb_array
				rgb_array += redBinString + greenBinString + blueBinString
				
				secretMessageIndex += 3
			else:
				return

def newFile():
	secretData = ""
	byteAray = []

	#iterate through the size of the secret message and stre the last bits into secretData
	for i in range(secretMessageSize):
		secretData += rgb_array[i]

	print len(secretData)
	print secretData

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