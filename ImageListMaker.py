import random
import os
from sets import Set
from SETTINGS import *

class ImageListMaker:
    '''Class for generating a list of random images from a collection'''

    def __init__(self):
        self.img_set = Set()
        self.folder = []
        self.weight = []
        for cat in IMAGES_CATEGORIES:
            self.folder.append(cat)
            self.weight.append(IMAGES_CATEGORIES[cat])
        
    def getImageList(self):
        if len(self.img_set) < 1:
            self.generateImageList()
        return list(self.img_set)
    
    def generateImageList(self, num=10):
        img_data = os.path.join(IMAGES_FOLDER, self.get_random_picture())
        self.img_set.add(img_data)
        if len(self.img_set) < num:
            self.generateImageList()
    
    def get_random_picture(self):
        folder_cat = self.folder[self.weighted_choice_sub(self.weight)]
        picture = os.path.join(folder_cat, random.choice(os.listdir(os.path.join(IMAGES_FOLDER, folder_cat))))
        if(picture.endswith("jpg") == False):
            picture = self.get_random_picture()
        return picture

    #http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/        
    def weighted_choice_sub(self, weights):
        rnd = random.random() * sum(weights)
        for i, w in enumerate(weights):
            rnd -= w
            if rnd < 0:
                return i
