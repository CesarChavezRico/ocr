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


from PIL import Image
import glob
import os

redYpercent = .07
redXpercent = .45

blueYpercent = .09
blueXpercent = .55

greenYpercent = .15
greenXpercent = .65


d = os.path.dirname(__file__)
images = glob.glob('{0}/*.jpg'.format(d))

for image_path in images:
    image = Image.open(image_path)

    # Determine cut size based on type of image
    # cut_size (portionX, portionY)
    if 'red' in image_path:
        text = 'red'
        cut_size = (image.size[0]*redXpercent, image.size[1]*redYpercent)
    elif 'blue' in image_path:
        text = 'blue'
        cut_size = (image.size[0]*blueXpercent, image.size[1]*blueYpercent)
    elif 'green' in image_path:
        text = 'green'
        cut_size = (image.size[0]*greenXpercent, image.size[1]*greenYpercent)

    print ('Image Size ({1}) = {0}'.format(image.size, text))

    # image_center (centerX, centerY)
    image_center = image.size[0]/2, image.size[1]/2
    print image_center

    # order in which we specify the coordinates is:
    # startX, startY, endX, endY
    box = (int(image_center[0]-cut_size[0]/2), int(image_center[1]-cut_size[1]/2),
           int(image_center[0]+cut_size[0]/2), int(image_center[1]+cut_size[1]/2))
    cropped = image.crop(box)

    cropped.show()
