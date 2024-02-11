import os
import matplotlib.pyplot as plt
from keras.models import load_model
from deep_learning.model import create_model

def save_model(model, model_path):
    """Save the trained model to a file."""
    model.save(model_path)
    print(f"Model saved to: {model_path}")

def load_saved_model(model_path):
    """Load a saved model from a file."""
    if os.path.exists(model_path):
        model = load_model(model_path)
        print(f"Model loaded from: {model_path}")
        return model
    else:
        print(f"Error: Model file not found at {model_path}")
        return None

def plot_training_curves(history):
    """Plot training and validation curves."""
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.show()

    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()
    plt.show()
