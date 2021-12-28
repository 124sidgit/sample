#import os module 
import os

#this code find any file in your drive(Note:But we have to give the extension as well)
#Here r=root directory, d=a list with the subdirectories in the root directory, f=a list with all the files in the root directory
target=str(input("Please give the name of the file which you want to find?>>"))
start="C:\\"
for r,d,f in os.walk(start):
    if (target in f):
        print(r+"\\"+target)