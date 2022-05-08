import os
import glob
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 
import tensorflow as tf 

# path: path to folder of images
def get_formatted_images(path, cnt):
    image_list = []
    for idx, file_name in enumerate(glob.glob(path + '/*.png')):
        if idx >= cnt:
            break

        img = np.array(Image.open(file_name))

        # if len(img.shape) > 2:
        #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        h, w, d = img.shape
        min_dim = min(h, w)
        img = img[0:min_dim, 0:min_dim]

        image_list.append(img)
    return image_list

def split_train_test(images, percent_train):
    num_imgs = len(images)
    num_train = percent_train * num_imgs
    
    train_imgs = images[:num_train]
    test_imgs = images[num_train:]

    return (train_imgs)

def get_labels(images, label):
    labels = [label] * len(images)
    return labels

def normalize_images(images):
    return images / 255.0

        
if __name__ == "__main__":
    path = 'archive\\Recaptcha Dataset\\Bicycle'
    for img in get_formatted_images(path, cnt=5):
        plt.imshow(img)
    

