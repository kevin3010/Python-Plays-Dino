# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:49:21 2019

@author: Kevin Jivani

This is the class to prepare data for the training,
you need to change the the values of jumpPath and noJumpPath
for preparing testing data and the training data.

Also create the object.
"""
import os
import cv2
import numpy as np
from tqdm import tqdm

class JumpVSNoJump(object):
    
#    jumpPath = "images/testJump" #chage the value of the path to testJump
#    nojumpPath = "images/testNoJump" #change the value of the path to testNoJump
    
    
    jumpPath = "images/jump" #chage the value of the path to testJump
    nojumpPath = "images/no" #change the value of the path to testNoJump
        
    image_width = 80
    image_height = 80
    
    
    
    labels = {jumpPath : 0 , nojumpPath : 1}
    
    training_data = []
    
    jumpCount = 0
    noJumpCount = 0
    
    def make_train_data(self):
        for label in self.labels:
            print(label)
            for f in tqdm(os.listdir(label)):
                if "jpg" in f:
#                    try:
                    path = os.path.join(label,f)
                    img = cv2.imread(path,)
                    img = cv2.resize(img,(self.image_width,self.image_height))
                    self.training_data.append([np.array(img),np.eye(2)[self.labels[label]]])
                    
                    if label == self.jumpPath:
                        self.jumpCount += 1 
                    else:
                        self.noJumpCount += 1
                    
#                    except Exception as e:
#                        print("no successful")
                    
        np.random.shuffle(self.training_data)
#        np.save("testing_data.npy", self.training_data) #change the value for "training_data.npy" to "testing_data.npy"
        np.save("training_data.npy", self.training_data)
        print('Jump:',self.jumpCount)
        print('NoJump:',self.noJumpCount)
        
#a = JumpVSNoJump()
#a.make_train_data()
training_data = np.load('training_data.npy',allow_pickle=True)
print(training_data[0][0].shape)

testing_data = np.load('testing_data.npy',allow_pickle=True)
print(testing_data.shape[:])