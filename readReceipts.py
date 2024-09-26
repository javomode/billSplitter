'''
GOAL: read receipts using OpenCV and pytesseract
IDEA:
    1. Use edge detection to outline receipt against the background. (we need enough contrast to detect the receipt)
    2. Detect and identify contours
        a. The receipt will have 4 contours since it is a rectangle.
    3. Apply perspective transform so we get a bird's eye view of the receipt to improve OCR accuracy.
    4. Apply Pytesseract OCR on the bird's eye view to get the line-by-line of the contents.
    5. Parse item names and their prices.
    6. Display and contain the results.
'''
import pytesseract
import argparse
import imutils
import cv2
import re


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="testingReceipts/data/test/3UC3LAG60J49.JPG")
ap.add_argument("-d", "--debug", type=int, default=-1,
	help="whether or not we are visualizing each step of the pipeline")
args = vars(ap.parse_args())
