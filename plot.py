import matplotlib 
import matplotlib.pyplot as plt
import cv2
import numpy as np

img1 = cv2.imread("gallery/random2.png")
img2 = cv2.imread("gallery/bright2.jpeg")



array=np.array(img2)
print(array.shape)
# convert, but this is buggy 
img_hsv = matplotlib.colors.rgb_to_hsv(array[...,:3])
# pull out just the s channel
lu=img_hsv[...,2].flatten()
plt.hist(lu,256)
plt.show()


