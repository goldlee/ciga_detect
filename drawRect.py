import cv2

img = cv2.imread('ssss.jpg')
# cv2.rectangle(img, (589, 900), (624, 960), (0, 255, 0), 2)
# cv2.imshow('sd', img)
# cv2.waitKey(0)

cv2.line(img, (589, 900), (624, 900), (255, 0, 0), 4)
cv2.imwrite('sda2.jpg', img)