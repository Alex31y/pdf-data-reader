# We import the necessary packages
# import the needed packages
import cv2
import os
import pytesseract
from PIL import Image

def to_text(tesseract, img):
    pytesseract.pytesseract.tesseract_cmd = tesseract

    # We then read the image with text
    images = cv2.imread(img)

    # convert to grayscale image
    gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

    # checking whether thresh or blur

    cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    #cv2.medianBlur(gray, 3)

    # memory usage with image i.e. adding image to memory
    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    """
    print(text)
    # show the output images
    cv2.imshow("Image Input", images)
    cv2.imshow("Output In Grayscale", gray)
    cv2.waitKey(0)
    """
    return text

