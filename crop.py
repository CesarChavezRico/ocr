"""
crop size is determined as a function of the image size, type of image (red, green, blue .. see CL photo app) and
the relative size of the region of interest in both X and Y. It is also assumed that the region of interest is in the
approximate center of the original image

Y:
good -- blue: 300 of 3264               <--- 9%

(needs zoom out) -- green: 300 of 3264

(needs zoom in) -- red 300 of 3264
good -- red: 300 of 4160                <--- 7%
good -- red: 300 of 4160                <--- 7%


X:
good -- blue: 1200 of 2448              <--- 49%

(needs zoom out) -- green: 1400 of 2448

(needs zoom in) -- red: 1000 of 3264
good -- red: 1000 of 4160               <--- 24%
good -- red: 1000 of 4160               <--- 24%



"""


import cv2
import glob
import os

redYpercent = .07
redXpercent = .24

blueYpercent = .09
blueXpercent = .45

greenYpercent = .15
greenXpercent = .65


d = os.path.dirname(__file__)
images = glob.glob('{0}/*.jpg'.format(d))

for image_path in images:
    image = cv2.imread(image_path)

    # Determine cut size based on type of image
    if 'red' in image_path:
        text = 'red'
        cut_size = (image.shape[1]*redYpercent, image.shape[0]*redXpercent)
    elif 'blue' in image_path:
        text = 'blue'
        cut_size = (image.shape[1]*blueYpercent, image.shape[0]*blueXpercent)
    elif 'green' in image_path:
        text = 'green'
        cut_size = (image.shape[1]*greenYpercent, image.shape[0]*greenXpercent)

    print ('Image Size ({2}) = {0}, {1}'.format(image.shape[1], image.shape[0], text))

    # order in which we specify the coordinates is:
    # startY:endY, startX:endX

    image_center = image.shape[0]/2, image.shape[1]/2

    cropped = image[image_center[0]-cut_size[0]/2:image_center[0]+cut_size[0]/2,
                    image_center[1]-cut_size[1]/2:image_center[1]+cut_size[1]/2]

    cv2.imshow("Cropped - {0}".format(text), cropped)
    cv2.waitKey(0)