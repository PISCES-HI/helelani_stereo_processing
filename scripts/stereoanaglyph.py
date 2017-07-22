
from PIL import Image, ImageChops, ImageMath
import math
import sys
from PIL import ImageOps
from PIL.ImageOps import grayscale
from PIL.ImageOps import colorize

def Anaglyph(imgl, imgr):
	right = imgr
	left = imgl
	width, height = left.size
	leftMap = left.load()
	rightMap = right.load()

	left = grayscale(left)
	left = colorize(left, (0,0,0),(255,0,0))

	right = grayscale(right)
	right = colorize(right, (0,0,0),(0,255,255))

	anagimg = Image.blend(left,right,0.5)

	return anagimg

if __name__ == '__main__':
    imgind = 0
    imgind1 = 0
    if len(sys.argv) > 1:
        imgind = sys.argv[1]
        imgind1 = sys.argv[2]
        Anaglyph(imgind, imgind1)