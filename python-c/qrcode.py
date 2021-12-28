#import qrcode module
import qrcode

#Make a variable data in which we can store our information which we want to convert in qrcode
#And put the link of any website here
data="Name=Sid\nDOB=00/00/0000\nCountry=Globe"

#Here the data is converted into qrcode
img=qrcode.make(data)

#And here it is save in the address given by us
img.save("C:/Users/sis-s/Desktop")
