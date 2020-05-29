from tkinter import Image
from PIL import Image, ImageFilter
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image
import sys

img = Image.open("Foto/foto.png")
img = img.convert("RGBA")
from PIL import Image

imagePath = "Foto/foto.png"
#newImagePath = 'A:\ex2.jpg'
im = Image.open(imagePath)

def redOrBlack (im):
    newimdata = []
    redcolor = (0, 0, 0)
    redcolor1 = (105, 105, 105)

    blackcolor = (255,0,0)
    for color in im.getdata():
        if color >= redcolor or color <= redcolor1:
            newimdata.append( (0,125,0) )
        else:
            newimdata.append( color)
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

    redOrBlack(im).save("Faces/fotso.png")
#img.save("Faces/foto.png")