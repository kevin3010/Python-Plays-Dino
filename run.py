# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:41:36 2020

@author: Kevin Jivani
"""

import pyautogui
from tensorflow.keras.models import load_model

from grabscreen import grab_screen
from getkeys import key_check
import cv2   
import time
import numpy as np
import random


def waitBeforeCapturingScreen():
    count = 0
    while(count!=0): 
        
        key = key_check()
    
        if 'up' in key or 'space' in key:
            count += 1
        print(key)
    print("ScreenRecording Started")
    time.sleep(2)

flag = 0

model = load_model("./model/dino_model")

print("Started")
while(flag==0):
    img = grab_screen((1,260,750,480))
    img = cv2.resize(img,(80,80))
    
    img = np.asarray(img,dtype=float)
    img = img.astype('float32')/255
    img = img[np.newaxis, :]
      
    prediction = model.predict(img)
#    print(prediction)
    
    if(prediction[0][0]>0.20):                
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        print("Jump "+str(prediction[0][0]))
    else:
        pass