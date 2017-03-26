import cv2
import sys
import numpy as np

image_path = sys.argv[1]
template_path = sys.argv[2]

img_rgb = cv2.imread(image_path)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(template_path,0)
w, h = template.shape[::-1]
w_img, h_img = img_gray.shape[::-1]

if (w_img < w) or (h_img < h):
    if (h - h_img) >= (w - w_img):
        h_note = 0.11 * h_img
        scalefactor = h_note / h
        res = cv2.resize(template, None, fx=scalefactor, fy=scalefactor, interpolation = cv2.INTER_AREA)
    else:
        print "Please use a template image with width less than %d" % w_img

res = cv2.matchTemplate(img_gray,res,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('Images/res.png',img_rgb)