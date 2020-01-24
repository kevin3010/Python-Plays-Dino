# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 09:31:14 2019

@author: Kevin Jivani
"""

from grabscreen import grab_screen
from getkeys import key_check
import cv2 
import time
import numpy as np


def waitBeforeCapturingScreen():
    count = 0
    while(count!=0): 
        
        key = key_check()
    
        if 'up' in key or 'space' in key:
            count += 1
        print(key)
    print("ScreenRecording Started")
    time.sleep(2)

#screen = grab_screen((1,260,750,480))
#cv2.imwrite("test.jpg",screen)
#screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
#screen = cv2.resize(screen, (80,60))
#cv2.imwrite("./images/up/up-"+str(i)+".jpg",screen)
waitBeforeCapturingScreen()  


jump = 0 
#dump = 0 
space = 0 
no = 0
while(jump<1000 or no<1000):
    
    screen = grab_screen((1,260,750,480))
    
    key = key_check()

    
    if 'jump' in key:
        if jump<1000:   
            cv2.imwrite("./images/jump/jump-"+str(jump)+".jpg",screen)
            jump += 1
            print('jump'+str(jump))
            
    else:
        if no<1000 :
            cv2.imwrite("./images/no/no-"+str(no)+".jpg",screen)
            no += 1

#    elif 'dump' in key:
#        if dump<10:
#            cv2.imwrite("./images/dump/dump-"+str(dump)+".jpg",screen)
#            dump += 1
#            print()
    
#    elif 'space' in key:
#        if space<10:
#            cv2.imwrite("./images/space/space-"+str(space)+".jpg",screen)
#            space += 1
#            print('space'+str(space))


print("done")
    