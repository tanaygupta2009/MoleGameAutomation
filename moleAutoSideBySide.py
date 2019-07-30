#from imagesearch import *
from pyautogui import *
import time
import os,sys
import socket
import cv2
import random
import numpy as np
from PIL import Image


def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1

    return screenshot(region=(x1,y1,width,height))
def imagesearcharea(image, x1,y1,x2,y2, precision=0.8, im=None) :
    if im is None :
        im = region_grabber(region=(x1, y1, x2, y2))
        im.save('testarea.png') #to debug

    img_rgb = np.array(im)
    #print img_rgb
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #print 'Image Gray'
    r=Image.fromarray(img_gray)
    r.save('lmao.png')
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

def imagesearch(image, precision=0.8):
    im = screenshot()
    #im.save('testarea.png') to debug
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    #print(template.shape)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc


count=0
while(1):
    pic = imagesearch("mole2.png")
    if(pic[0]==-1):
        print("Mole Not Found")
        count+=1
    else:
        count=0
        print(pic)
        moveTo(pic[0]+5,pic[1]+5)
        click()
        '''
    if(count>=25):
        print("I Think the game is already ended...exiting now")
        break
        '''


    
