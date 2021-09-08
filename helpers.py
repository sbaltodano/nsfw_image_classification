# -*- coding: utf-8 -*-
"""helpers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jkJaLbXp6j89K46voNBTpyQquoeBO_EX
"""

import matplotlib.pyplot as plt

# create a function to reuse for plotting accuracy and loss per epoch
def plot_model_train_accuracy_loss(model_score):

    # summarize history for accuracy
    plt.plot(model_score.history['accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(model_score.history['loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

# create a function to reuse for plotting accuracy and loss per epoch
def plot_model_train_val_accuracy_loss(model_score):

    # summarize history for accuracy
    plt.plot(model_score.history['accuracy'])
    plt.plot(model_score.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(model_score.history['loss'])
    plt.plot(model_score.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()