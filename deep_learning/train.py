#This script trains the model on the prepared dataset.

from keras.optimizers import Adam
from deep_learning.model import create_model
from deep_learning.data_preprocessing import *


if __name__ == "__main__":

    dataset_path = '/dataset'
    image_size = (520, 520)  
    images, labels = preprocess_dataset(dataset_path, image_size)

    model = create_model()
    model.compile(optimizer=Adam(lr=0.001),
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(images, labels, batch_size=32, epochs=10, validation_split=0.2)