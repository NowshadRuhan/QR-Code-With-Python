import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image

s = "Nowshad Ruhani Chowdhury, Lead Software Engineer."

url = pyqrcode.create(s)

url.svg("mycode.svg", scale = 8)

url.png("mycode.png", scale = 6)

img = Image.open(r"C:\Users\HP\Desktop\Python Project\mycode.png") 
 
img.show()

display(img)