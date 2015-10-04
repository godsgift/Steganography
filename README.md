# Steganography
Before running the programs, make sure that python 2.7 or above is installed
Note: this was tested on python version 2.7.8
We used the Pillow library for the image manipulation part of the program
To install, make sure you have pip installed (usually comes with Python)
############################
pip install Pillow
############################

Once you have python and Pillow library installed, we can then run the programs

To run stegosaurus.py, we will need to supply it with 3 arguments
############################
python stegosaurus.py [cover image] [data we want to hide] [output file we want]

Note: the outputfile must be an image with a .bmp extension
example:
python stegosaurus.py red.bmp fb.bmp hidden.bmp
############################

To run destegosaurus.py, we will need to supply it with 1 argument
############################
python destegosaurus.py [modified image with the secret data]

example:
python destegosaurus.py hidden.bmp
############################
