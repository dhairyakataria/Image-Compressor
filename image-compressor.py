import PIL
from PIL import Image

mywidth = 2000

img = Image.open("C:/Users/dhairya.kataria/Pictures/original IC/IMG_20231001_160046.jpg")

width_per = (mywidth/float(img.size[0]))
h_size = int(float(img.size[1])*float(width_per))
img_1 = img.resize((mywidth, h_size), Image.Resampling.LANCZOS)
img_1.save("C:/Users/dhairya.kataria/Pictures/original IC/compressed_1.jpg")
# img.show()
# img_1.show()