from PIL import ImageGrab
import cv2
import numpy as np

screenshot = ImageGrab.grab()
# screenshot.show()

cv_img = np.array(screenshot)
cv_img = cv_img[:, :, ::-1].copy()

cv2.imshow("screen", cv_img)
cv2.waitKey(0)