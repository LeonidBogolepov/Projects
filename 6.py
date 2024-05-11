import math
import pandas as pd
import cv2
import numpy as np
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image
import matplotlib.pylab as plt

url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Chess_board_opening_staunton.jpg"


img_color = io.imread(url)
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
cv2_imshow(img)
cv2_imshow(img_color)

def moravec_points(src, color_src, window_size=5, threshold=5000):
  mor_image = color_src.copy()
  r = window_size // 2
  rows = mor_image.shape[0]
  cols = mor_image.shape[1]
  corners = []

  for y in range(r, rows-r):
    for x in range(r, cols-r):
      wV1 = 0; wV2 = 0; wV3 = 0; wV4 = 0;
      for k in range(-r, r): # 0 degree
        wV1 += (src[y, x+k] - src[y, x+k+1])*(src[y, x+k] - src[y, x+k+1])
      for k in range(-r, r): # 90 degree
        wV2 += (src[y+k, x] - src[y+k+1, x])*(src[y+k, x] - src[y+k+1, x])
      for k in range(-r, r): # 45 degree
        wV3 += (src[y+k, x+k] - src[y+k+1, x+k+1])*(src[y+k, x+k] - src[y+k+1, x+k+1])
      for k in range(-r, r): # 135 degree
        wV4 += (src[y+k, x-k] - src[y+k+1, x-k-1])*(src[y+k, x-k] - src[y+k+1, x-k-1])
      arr = np.array([wV1, wV2, wV2, wV2])
      val = 0
      val = min(arr)
      if val > threshold:
        corners.append((x, y))

  print(f'Corners: {len(corners)}')
  for corner in corners:
    cv2.circle(mor_image, corner, 3, (0, 255, 0))
  return mor_image

mor_image = moravec_points(img, img_color, 5, 500)
cv2_imshow(mor_image)

if sys.path[0] == '':
    Corners: 1321

url = "https://cdn.shopify.com/s/files/1/1297/3303/products/21-folding-hardwood-player-s-chessboard-jlp-usa-3536024272972_1024x.jpg?v=1575932159"

img_color = io.imread(url)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

operatedImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
operatedImage = np.float32(operatedImage)
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
dest = cv2.dilate(dest, None)
img[dest > 0.001 * dest.max()] = [0, 0, 255]

cv2_imshow(img)

url = "https://cdn.shopify.com/s/files/1/1297/3303/products/21-folding-hardwood-player-s-chessboard-jlp-usa-3536024272972_1024x.jpg?v=1575932159"

img_color = io.imread(url)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
operatedImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(operatedImage,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )

cv2_imshow(img2)