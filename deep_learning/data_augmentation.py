#This script performs data augmentation to increase the diversity of the dataset.

from keras.preprocessing.image import ImageDataGenerator
from deep_learning.data_preprocessing import *
import numpy as np

def augment_dataset(images, labels):
    """Augment the dataset using various techniques."""
    augmented_images = []
    augmented_labels = []
   
    images = np.array(images)
    labels = np.array(labels)

    datagen = ImageDataGenerator(rotation_range=20,
                                 width_shift_range=0.2,
                                 height_shift_range=0.2,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip=True,
                                 fill_mode='nearest')

    datagen.fit(images)

    for X_batch, y_batch in datagen.flow(images, labels, batch_size=len(images), shuffle=False):
        augmented_images.extend(X_batch)
        augmented_labels.extend(y_batch)
        break  
    return augmented_images, augmented_labels

if __name__ == "__main__":

    augmented_images, augmented_labels = augment_dataset(images, labels)



