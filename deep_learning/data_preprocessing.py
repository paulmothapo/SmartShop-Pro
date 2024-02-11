#This script handles data preprocessing tasks such as loading images, resizing, normalizing, and preparing the dataset for training.

import numpy as np
import cv2
import os
from pyzbar.pyzbar import decode


def load_images_from_directory(directory_path, image_size):
    """Load images from a directory and preprocess them."""
    images = []
    labels = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            img_path = os.path.join(directory_path, filename)
            try:
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, image_size)
                    img = img.astype('float32') / 255.0 
                    images.append(img)
                    labels.append(filename.split("_")[0])
                else:
                    print(f"Failed to load image: {img_path}")
            except Exception as e:
                print(f"Error processing image {img_path}: {str(e)}")
    return np.array(images), np.array(labels)


def preprocess_dataset(directory_path, image_size):
    """Preprocess the entire dataset."""
    if not os.path.isdir(directory_path):
        print(f"Directory not found: {directory_path}")
        return None, None
    images, labels = load_images_from_directory(directory_path, image_size)
    if len(images) == 0:
        print("No images found in the directory.")
    return images, labels


def live_barcode_scanning(output_directory):
    """Scan for barcodes using webcam and save the captured image."""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray)
        for obj in decoded_objects:
            print("Detected Barcode:", obj.data.decode('utf-8'))
            cv2.rectangle(frame, (obj.rect.left, obj.rect.top), 
                          (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (255, 0, 0), 2)

            filename = os.path.join(output_directory, f"scanned_image_{obj.data.decode('utf-8')}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")
        cv2.imshow('Barcode Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    dataset_path = "deep_learning/dataset/class1"
    output_directory = "deep_learning/scanned_data"  
    if not os.path.exists(dataset_path):
        print(f"Dataset path not found: {dataset_path}")
    else:
        image_size = (520, 520)
        images, labels = preprocess_dataset(dataset_path, image_size)
        if images is not None:
            print(f"Preprocessed {len(images)} images.")
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            live_barcode_scanning(output_directory)

