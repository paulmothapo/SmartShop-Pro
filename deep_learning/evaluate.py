#This script evaluates the trained model's performance on a separate test set.

from deep_learning.model import create_model
from deep_learning.data_preprocessing import *

if __name__ == "__main__":

    if not create_model:
        print("Error: Model not available for evaluation.")
    elif not images or not labels:
        print("Error: Test data not available for evaluation.")
    else:
        loss, accuracy = create_model.evaluate(images, labels)
        print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")
        

