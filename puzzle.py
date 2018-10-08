import cv2
import numpy as np
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
im_path = os.path.join(this_dir,
                       'test',
                       'images',
                       '1.jpg')

if not os.path.exists(im_path):
    raise FileNotFoundError

img = cv2.imread(im_path, 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

