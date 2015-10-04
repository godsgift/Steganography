from PIL import Image
import PIL.ImageOps
import sys
import array
import binascii

def usage():
    if len(sys.argv) !=  2:
        print "To use: ", sys.argv[0], "ModifiedImage"
        sys.exit()


def destegosaurus():
	global secretMessageSize
	global fileName
	global dataHolder
	modifiedImage = str(sys.argv[1])
	rgb_array = ""
	secretImage = Image.open(modifiedImage)
	rgb_img = secretImage.convert('RGB')
	width, height = rgb_img.size

	secretMessageSize = 0
	secretMessageIndex = 0
	dataHolder =""
	fileName = ""
	byte = ""
	byteList = []
	nullCondition = "00000000"
	nullCounter = 0

	#iterate through all the pixels
	for x in range(width):
		for y in range(height):
			#grab the RGB of each pixels
			r, g, b = rgb_img.getpixel((x, y))
			#change the RGB into binary
			redBinString = str(bin(r)[2:].zfill(8))[7]
			greenBinString = str(bin(g)[2:].zfill(8))[7]
			blueBinString = str(bin(b)[2:].zfill(8))[7]
			#add the binary into a list
			rgb_array = [redBinString, greenBinString, blueBinString]

			#loop through the length of rgb_array
			for i in range(len(rgb_array)):
				byte += rgb_array[i]
				if len(byte) == 8:
					byteList.append(byte)
					#if it sees the null terminator, we grab the file name before it
					if (byte == nullCondition and nullCounter == 0):
						fileName = ''.join(binascii.unhexlify('%x' % int(b,2)) for b in byteList[0:len(byteList) - 1])
						byteList = []
						nullCounter += 1
					#if it sees another null terminator, we grab the data size
					elif (byte == nullCondition and nullCounter == 1):
						secretMessageSize = ''.join(binascii.unhexlify('%x' % int(b,2)) for b in byteList[0:len(byteList) - 1])
						byteList = []
						nullCounter += 1
						continue;
					byte = ""
				if (nullCounter == 2):
					#put into dataHolder all the hidden data
					if int(secretMessageIndex) < int(secretMessageSize):
						dataHolder += rgb_array[i]
						secretMessageIndex += 1
					else:
						return

def newFile():
	secretData = ""
	#iterate through the size of the secret message and add the last bits into secretData
	for i in range(int(secretMessageSize)):
		secretData += dataHolder[i]

	newByteArray = []
	#grab chunks of 8 bits and store it into newByteArray
	for i in range (0, len(secretData)/8):
		newByteArray.append(int(secretData[i*8:(i+1) * 8], 2))

	#change everything in newByteArray into decimal values and store into byteArray
	byteArray = array.array('B', newByteArray).tostring()
	
	secretMessage = bytearray(byteArray)
	#write the file
	createFile = open("DecodedData/" + fileName, 'wb')
	createFile.write(secretMessage)

if __name__ == "__main__":
	usage()
	destegosaurus()
	newFile()
