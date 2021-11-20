import cv2
import numpy as np

mush = cv2.imread('./data/mushroom.jpg')
logo = cv2.imread('./data/cvlogo.png')

print(logo.shape)
logo = cv2.resize(logo, (logo.shape[1] // 2, logo.shape[0] // 2))

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
retval, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

roi = mush[:logo.shape[0], :logo.shape[1]]
mask_inv = cv2.bitwise_not(mask)

bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
fg = cv2.bitwise_and(logo, logo, mask=mask)
combined = cv2.add(fg, bg)
mush[:combined.shape[0], :combined.shape[1]] = combined

cv2.namedWindow("Image", cv2.WINDOW_KEEPRATIO)
cv2.imshow("Image", mush)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(mush.shape)
print(logo.shape)
