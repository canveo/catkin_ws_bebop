#!/usr/bin/env python
from __future__ import print_function
import cv2
import numpy as np
import rospkg
import json
import matplotlib.pyplot as plt


rospack = rospkg.RosPack()

config_path = str(rospack.get_path('cv_detection')+'/config/feature_config.json')
images_path = str(rospack.get_path('cv_detection')+'/config/img/')

class feature_detection():
    def __init__(self,image_name="H.png"):

        
        #load the image   
        self.source_image = cv2.imread( images_path + image_name,cv2.IMREAD_GRAYSCALE )
        print(self.source_image.shape)

                
        # Initiate ORB detector
        self.orb = cv2.ORB_create()

        self.ref_key_points, self.ref_description =  self.orb.detectAndCompute(self.source_image,None)


        # FLANN parameters
        # FLANN_INDEX_KDTREE = 1
        # index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        # search_params = dict(checks=5)   # or pass empty dictionary
        # # create BFMatcher object
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # self.flann = cv2.FlannBasedMatcher(index_params,search_params)
        #configure plt
        plt.ion()
        plt.show()
    
    def get_rect(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(image.shape)
        key_points, description =  self.orb.detectAndCompute(image,None)

        #calculate matches between 2 descriptions
        matches = self.bf.match(self.ref_description,description)
        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)


        img3 = cv2.drawMatches(self.source_image,self.ref_key_points,image,key_points,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        plt.imshow(img3,)
        plt.draw()
        plt.pause(0.001)


def main():

    print("init")
    f = feature_detection()

if __name__ == '__main__':
    main()