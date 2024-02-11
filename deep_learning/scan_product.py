import sys
from model import *
from utils import preprocess_image
from data_preprocessing import *

def recognize_product(barcode):


    dataset_path = '/dataset'
    image_size = (520, 520)  
    images, labels = preprocess_dataset(dataset_path, image_size)
    
    preprocessed_image = preprocess_image(barcode)

    recognized_product = model.predict(preprocessed_image)

    return recognized_product

if __name__ == '__main__':
    barcode = sys.argv[1]
    recognized_product = recognize_product(barcode)
    print(recognized_product)
