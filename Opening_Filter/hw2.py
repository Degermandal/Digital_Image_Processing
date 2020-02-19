import cv2
import numpy as np

#Dilate
def dilation(image):
    height = int(image.shape[0])
    width = int(image.shape[1])
    copy = image.copy()
    copy *= 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            if(image[i][j] == 255):
                copy[i-1:i+2, j-1:j+2] = 255
    return copy

#Erode
def erosion(image):
    kernel = np.ones((3,3))
    kernel = kernel*255
    height = int(image.shape[0])
    width = int(image.shape[1])
    copy = image.copy()
    copy *= 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            if(np.array_equal(kernel,image[i-1:i+2, j-1:j+2])):
                copy[i][j] = 255
            else:
                copy[i][j] = 0
    return copy

#Path Opening
def opening(image):
    pathOpening = dilation(erosion(image))
    return pathOpening

###the 3x3 kernel
grayscaleImage1 = cv2.imread("GrayscaleImages/GrayscaleApple.jpg", 0)
(height,width) = grayscaleImage1.shape

grayscaleImage2 = cv2.imread("GrayscaleImages/GrayscaleGirl.jpg", 0)
(height,width) = grayscaleImage2.shape
#...
binaryImage1 = cv2.imread("BinaryImages/BinaryApple.jpg", 0)
(height, width) = binaryImage1.shape

binaryImage2 = cv2.imread("BinaryImages/BinaryGirl.jpg", 0)
(height, width) = binaryImage2.shape

###Converting image to binary
ret, grayscale1 = cv2.threshold(grayscaleImage1, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('grayscaleToBinaryApple.jpg', grayscale1)

ret, grayscale2 = cv2.threshold(grayscaleImage2, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('grayscaleToBinaryGirl.jpg', grayscale2)

###Opening
opening1 = opening(grayscale1)
cv2.imwrite('resultGrayscaleApple.jpg',opening1)

opening2 = opening(grayscale2)
cv2.imwrite('resultGrayscaleGirl.jpg',opening2)
#...
opening3 = opening(binaryImage1)
cv2.imwrite('resultBinaryImageApple.jpg',opening3)

opening4 = opening(binaryImage2)
cv2.imwrite('resultBinaryImageGirl.jpg',opening4)

print("Successfully Completed")
