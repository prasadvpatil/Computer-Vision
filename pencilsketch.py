import cv2
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)
img = cv2.imread('capture.png',1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
final_img = dodgeV2(img_gray, img_smoothing)
cv2.imwrite('pencil_sketch_capture.png', final_img)