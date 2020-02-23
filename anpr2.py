import cv2
import random
import os
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

from skimage import filters




images_dir = "data/images"
image_files = os.listdir(images_dir)
image_path = "{}/{}".format(images_dir, "car_17.jpg")
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, bla) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

def plot_images(img1, img2, title1="", title2=""):
    fig = plt.figure(figsize=[7,4])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1, cmap="gray")
    ax1.set(xticks=[], yticks=[], title=title1)

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2, cmap="gray")
    ax2.set(xticks=[], yticks=[], title=title2)

plot_images(image, bla)



blur = cv2.bilateralFilter(bla, 25,105, 110)

plot_images(bla, blur)


img = cv2.GaussianBlur(bla,(3,3),0)

laplacian = cv2.Laplacian(img,cv2.CV_8UC1)

edges = cv2.Canny(img,100,100)

plot_images(blur, edges)
cv2.imwrite("data/images/blr.png", laplacian)


image_pat = "{}/{}".format(images_dir, "blr.png")

edg = cv2.imread(image_pat)

cnts, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

image_copy = image.copy()

_ = cv2.drawContours(image_copy, cnts, -1, (106,0,255),2)

plot_images(image, image_copy)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1000]

image_copy = image.copy()
_ = cv2.drawContours(image_copy, cnts, -1, (255,0,255),2)


plot_images(image, image_copy)
plate = None

for c in cnts:
    perimeter = cv2.arcLength(c, True)
    edges_count = cv2.approxPolyDP(c, 0.02 * perimeter, True)
    if len(edges_count) == 4:
        x,y,w,h = cv2.boundingRect(c)
        plate = image[y:y+h, x:x+w]
        break

cv2.imwrite("data/images/plate.png", plate)
plot_images(blur,img)
plt.show()








