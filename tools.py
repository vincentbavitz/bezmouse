import os
from time import time, sleep
from more_itertools import unique_everseen
from PIL import Image
from random import randint
from threading import Timer
from time import gmtime, strftime


#WORKING DIRECTORY
CWD = os.path.dirname(os.path.realpath(__file__))
 

def remove_dups(seq):
    return list(unique_everseen(seq))


def draw_points(points, width = 2000, height = 2000):
    '''
    Draws yellow crosses to a (default 2000x2000px) image for all coordinates in
    "points" argument
    saves to CWD as out-0000.png
    '''
        
    img = Image.new("RGB", (width, height))
    pix = img.load()
        
    try:
        for coords in points:
            pix[coords[0], coords[1]] = (255, 255, 0)
            pix[coords[0] + 1, coords[1] + 1] = (255, 255, 0)
            pix[coords[0] + 1, coords[1] - 1] = (255, 255, 0)
            pix[coords[0] - 1, coords[1] + 1] = (255, 255, 0)
            pix[coords[0] - 1, coords[1] - 1] = (255, 255, 0)

        img.save(CWD + '/tmp/out-' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
              + '.png')
    except:
        pass



