import cv2
import random
import os
import numpy as np
import matplotlib.pyplot as plt

import pytesseract


images_dir = "data/images"
image_files = os.listdir(images_dir)
image_path = "{}/{}".format(images_dir, "plate.png")


text = pytesseract.image_to_string(image_path, lang="eng")

f= open("data/images/number.txt","a +")


#f.write(text + " \n ")


print("The License Plate number is :- ")
print(text)