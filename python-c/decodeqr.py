#from PIL module import image and from pyzbar.pyzbar module import decode
from PIL import Image
from pyzbar.pyzbar import decode

#Give the address of the qrcode image in image variable that created earlier
img = Image.open("C:/Users/Desktop/etc.png")

#In result variable we have to call the decode fun to decode img
result = decode(img)
print(result)
