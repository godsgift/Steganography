from PIL import Image
import PIL.ImageOps
import sys
import array
import binascii

def usage():
    if len(sys.argv) !=  2:
        print "To use: ", sys.argv[0], "ModifiedImage"
        sys.exit()

def pixyGrabber():
	#Global variables
	global secretMessageSizeAscii
	global rgb_array
	global dataHolder
	global fileName_bytes
	#Image variables
	modifiedImage = str(sys.argv[1])
	rgb_array = ""
	secretImage = Image.open(modifiedImage)
	rgb_img = secretImage.convert('RGB')
	width, height = rgb_img.size
	rgb_array_list = []

	#misc variables
	nullCondition = "00000000"
	group = ""
	secretMessageSize = ""
	secretMessageIndex = 0
	nullCounter = 1
	temp = ""
	binStringSecretMsg = ""
	secretMessageSizeAscii = ""
	secretMsgInt = 0
	cCounter = 0
	dataHolder = ""

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
		#stores all the data into temp for now
		temp += i
		#if it sees the first null terminator, grab all the data before it and save it as file name
		if (i == nullCondition and nullCounter == 1):
			fileName_bytes = temp[0:len(temp) - 8]
			nullCounter += 1
			#reset temp
			temp = ""
		#if we see the second null terminator, we grab the data size from the data before the null terminator
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
			secretMsgInt = int(secretMessageSizeAscii)
			nullCounter += 1
			temp=""
		#grab the data depending on the data size that was given
		elif(nullCounter == 3):
			for k in range(secretMsgInt):
				dataHolder += group[cCounter+k]
			return
			nullCounter += 1
		cCounter += 1

def newFile():
	secretData = ""
	byteAray = []
	test = ""
	fileName = ""
	#grabs the file name and changes it back into a string
	fileName = ''.join(chr(int(fileName_bytes[i:i+8], 2)) for i in xrange(0, len(fileName_bytes), 8))
	#iterate through the size of the secret message and add the last bits into secretData
	for i in range(int(secretMessageSizeAscii)):
		secretData += dataHolder[i]

	#take out the extra bits that was being added after the hidden data
	#secretData = secretData[:-8]
	newByteArray = []

	#grab chunks if 8 bits and store it into newByteArray
	for i in range (0, len(secretData)/8):
		newByteArray.append(int(secretData[i*8:(i+1) * 8], 2))

	#change everything innewByteArray into decimal values and store into byteArray
	byteArray = array.array('B', newByteArray).tostring()
	#secret message is now 
	secretMessage = bytearray(byteArray)

	createFile = open("DecodedData/" + fileName, 'wb')
	createFile.write(secretMessage)

if __name__ == "__main__":
	usage()
	pixyGrabber()
	newFile()