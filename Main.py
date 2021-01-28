import png # Importing module for converting QR Code to PNG.
import pyqrcode # Importing module for generating QR Code.
from pyqrcode import QRCode # Importing QRCode function from the module.
import cv2 # Importing OpenCV to display the generated QR Code.
import os # Importing os to remove the generated image after usage.

a = input("Enter the link: ") # Taking the link as input from the user.
b = pyqrcode.create(a) # Generating QR Code from link.
b.png('QR_Code.png', scale=10) # Giving the image file a Name and a Scale.

Img = cv2.imread('QR_Code.png') # Making OpenCV read the image.
Window_Name = "Your QR Code" # Giving our OpenCV window a name.
cv2.imshow(Window_Name, Img) # Displaying the image.
cv2.waitKey(0) # Waiting for the key 0 to terminate the Program.
cv2.destroyAllWindows() # Terminating the Program
os.remove('QR_Code.png') # Removing the generated image file.