import cv2
import numpy as np
import pytesseract
import os

image_path = r"C:\Users\paull\Pictures\Sudoku.png"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def rectify(h):
        h = h.reshape((4,2))
        hnew = np.zeros((4,2),dtype = np.float32)

        add = h.sum(1)
        hnew[0] = h[np.argmin(add)]
        hnew[2] = h[np.argmax(add)]
        
        diff = np.diff(h,axis = 1)
        hnew[1] = h[np.argmin(diff)]
        hnew[3] = h[np.argmax(diff)]
 
        return hnew

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Edge detection
    thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
    return gray, thresh


if __name__ == '__main__':
    # Preprocess the image
    gray, thresh = preprocess_image(image_path)
    

    # Find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    # Sort contours by area and keep the largest one
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    print(len(contours))
    # Draw contours on the original image
    image = cv2.imread(image_path)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    biggest = None
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
                peri = cv2.arcLength(i,True)
                approx = cv2.approxPolyDP(i,0.02*peri,True)
                if area > max_area and len(approx)==4:
                        biggest = approx
                        max_area = area

    # Draw the biggest contour on the image
    #cv2.drawContours(image, biggest, -1, (0, 255, 0), 3)
    #cv2.drawContours(image, biggest, 1, (0, 255, 0), 3)
    #cv2.drawContours(image, biggest, 2, (0, 255, 0), 3)
    #cv2.drawContours(image, biggest, 3, (0, 255, 0), 3)

    approx=rectify(approx)

    

    h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)

    retval = cv2.getPerspectiveTransform(approx,h)
    warp = cv2.warpPerspective(gray,retval,(450,450))

    cv2.imshow('warp',warp)
    cv2.imshow('thresh',thresh)
    # Draw the contours on the image    

    # Show the result
    cv2.imshow("Contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    config = '--psm 6 --oem 3 -c tessedit_char_whitelist=123456789'
    detected_digits = pytesseract.image_to_string(warp, config=config)
    print("Detected digits:", detected_digits)

    # Write the detected digits into an array
    rows, cols = (9, 9)
    sudoku_array = [[0 for i in range(cols)] for j in range(rows)]
    detected_digits = detected_digits.replace('\n\n', '\n')
    detected_digits = detected_digits.split('\n')
    detected_digits.pop()


    print(detected_digits)