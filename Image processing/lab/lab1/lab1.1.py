import cv2
import numpy as np
import math
import matplotlib.image as mpimg

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 7))

# setting values to rows and column variables
rows = 2
columns = 4

img = cv2.imread("D:\Image processing\lab\pic\pokemonmaster.png")

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

B = (img[:, :, 0])
G = (img[:, :, 1])
R = (img[:, :, 2])

# 1.1 BGR vs RGB

# BGR
fig = plt.figure(figsize=(12, 7))
rows = 1
columns = 4
shapeimg = RGB_img.shape
tpimg = np.transpose(RGB_img)

fig.add_subplot(rows, columns, 1)
plt.imshow(RGB_img[:, :, 0], cmap='gray')
plt.title('X = (H, W, CH)\nX = {}\nR_Original'.format(shapeimg))
print('')

fig.add_subplot(rows, columns, 2)
plt.imshow(tpimg[:, :, 0], cmap='gray')
plt.title('X = (H, W, CH)\nX = {}\nR_Tranpose'.format(shapeimg))

plt.waitforbuttonpress()
plt.close('all')
