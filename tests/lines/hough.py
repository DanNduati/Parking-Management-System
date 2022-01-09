import os
import cv2
import numpy as np
from os.path import join

images_dir = join(os.getcwd(), 'images')
image = 'parking4.jpeg'

image = cv2.imread(f"{join(images_dir,image)}")

print('Original Dimensions : ', image.shape)

scale_percent = 60  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
print(lines)
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("lines", image)
cv2.imwrite(f"{join(images_dir,'houghlines.jpg')}", image)
cv2.waitKey(0)
