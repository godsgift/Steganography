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
	rgb_array_list = []

	nullCondition = "00000000"
	group = ""
	secretMessageSize = ""
	secretMessageIndex = 0
	nullCounter = 1

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
	temp = ""
	ss = ""
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
			cc = 0
			for j in range(len(secretMessageSizeList)/8):
				for i in range(0, 8):
					ss += secretMessageSizeList[cc]
					cc += 1
				print ss
				
				#print chr(test)
				ss = ""
			print ss

			nullCounter += 3

# 		elif secretMessageIndex <= int(secretMessageSize, 2):
# 			#grab the rgb values from the x and y values of the pixels
# 			r, g, b = rgb_img.getpixel((x, y))
# 			#change rgb into binary then grab the last bit and turn it into a string
# 			redBinString = str(bin(r)[2:].zfill(8))[7]
# 			greenBinString = str(bin(g)[2:].zfill(8))[7]
# 			blueBinString = str(bin(b)[2:].zfill(8))[7]
# 			#combine all the rgb string values and put it into rgb_array
# 			rgb_array += redBinString + greenBinString + blueBinString
			
# 			secretMessageIndex += 3
# 		else:
# 			return

# def newFile():
# 	secretData = ""
# 	byteAray = []

# 	#iterate through the size of the secret message and add the last bits into secretData
# 	for i in range(int(secretMessageSize)):
# 		secretData += rgb_array[i]

# 	print len(secretData)
# 	print secretData

# 	newByteArray = []
# 	#
# 	for i in range (0, len(secretData)/8):
# 		newByteArray.append(int(secretData[i*8:(i+1) * 8], 2))

# 	byteArray = array.array('B', newByteArray).tostring()
# 	secretMessage = bytearray(byteArray)

# 	createFile = open('test.txt', 'w')
# 	createFile.write(secretMessage)

if __name__ == "__main__":
	pixyGrabber()
	#newFile()