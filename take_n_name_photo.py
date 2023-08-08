import cv2
import os

# allow the user to input the names of images
imgs = []

while True:
    file = input("Input filename >>> ")
    if file == "QUIT":
        break
    if os.path.exists(file):
        img = cv2.imread(file)
        imgs.append(img)
    else:
        print("File not found.")
