__author__ = 'Cesar'

import numpy as np

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 4, figsize=(20, 8))
ax0, ax1, ax2, ax3 = axes


# ##### LINES APPROACH #####
def calculate_distance(p1, p2):
    import math
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def calculate_angle(p1, p2):
    import math
    try:
        return math.degrees(math.atan((p1[1] - p2[1])/(p2[0] - p1[0])))
    except ZeroDivisionError:
        return 90.0


def find_lines(image):
    from skimage.transform import probabilistic_hough_line
    lines = dict()

    lines_raw = probabilistic_hough_line(image)
    # Get metrics
    for ln in lines_raw:
        # Calculate length
        length = calculate_distance(ln[0], ln[1])
        # Calculate angle
        angle = calculate_angle(ln[0], ln[1])
        # fill dictionary ((x1,y1), (x2,y2)): (len, angle)
        lines[ln] = (length, angle)
    angles = [abs(lines.values()[0][1])]
    found = False
    for i, ln in enumerate(lines):
        if len(angles) > 0:
            for ang in angles:
                if (ang - 10.0) < abs(lines[ln][1]) and abs(lines[ln][1]) < (ang + 10.0):
                    found = True
                    break  # Already in list
            if found:
                found = False
            else:
                angles.append(abs(lines[ln][1]))
        else:
            print 'Lines: Empty Dict'

        print 'Lines [{0}] = {1:>30}:{2:<20}'.format(i, ln, lines[ln])
    print angles

from skimage.draw import line

img = np.zeros((250, 250, 3), dtype=np.uint8)
rr, cc = line(50, 50, 50, 200)
img[rr, cc, 0] = 0
img[rr, cc, 1] = 0
img[rr, cc, 2] = 255
rr, cc = line(50, 200, 200, 200)
img[rr, cc, 0] = 0
img[rr, cc, 1] = 255
img[rr, cc, 2] = 0
rr, cc = line(200, 200, 200, 50)
img[rr, cc, 0] = 255
img[rr, cc, 1] = 0
img[rr, cc, 2] = 0
rr, cc = line(200, 50, 50, 50)
img[rr, cc, 0] = 255
img[rr, cc, 1] = 255
img[rr, cc, 2] = 255

# Test with rotation
from skimage.transform import rotate
img = rotate(img, 1473.56)

ax0.set_title('Original')
ax0.imshow(img)


# From color image to gray scale
from skimage.color import rgb2gray
img_grey = rgb2gray(img)
ax1.set_title('Grey')
ax1.imshow(img_grey, cmap=plt.cm.gray)

# From gray scale, apply filter to get binary
from skimage.filters import threshold_adaptive
threshold = threshold_adaptive(img_grey, 1)
binary = img_grey > threshold
ax2.set_title('Binary')
ax2.imshow(binary, cmap=plt.cm.gray)

# Try skeletonize
from skimage.morphology import skeletonize
skeleton = skeletonize(binary)
ax3.set_title('Skeleton')
ax3.imshow(skeleton, cmap=plt.cm.gray)
find_lines(skeleton)





# # Try to find edges on grey scale
# from skimage.feature import canny
# edges = canny(img_grey)
# ax3.set_title('Edges')
# ax3.imshow(edges, cmap=plt.cm.gray)


# # Try to find edges on grey scale
# from skimage.filters import sobel
# edges = sobel(binary)
# ax3.set_title('Edges')
# ax3.imshow(edges, cmap=plt.cm.gray)
# find_lines(edges)

# Try Find contours
# from skimage import measure
# c = measure.find_contours(edges, 0.5, fully_connected='high')
# print 'Contours = {0}'.format(len(c))

# Try segmentation
# from skimage.segmentation import find_boundaries, mark_boundaries, felzenszwalb
# seg = felzenszwalb(binary)
# print 'Segments = {0}'.format(len(np.unique(seg)))
# segments = mark_boundaries(binary, seg)
# ax3.set_title('Segments')
# ax3.imshow(segments)




# plt.show()

