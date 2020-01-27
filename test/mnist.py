# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import logging

import pandas as pd
# ML imports
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
# To plot pretty figures
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

# DeepML imports
import tensorflow as tf
from tensorflow import keras

#Set Log
log = logging.Logger(__name__)
print("Working Dir" + os.path.curdir)

log_file_url= os.path.join(os.path.curdir + "mnsit.log")

logger = logging.getLogger(__name__)
f_handler = logging.FileHandler(log_file_url, mode='w' )
f_handler.setLevel(logging.DEBUG)

logger.addHandler(f_handler)

root_logdir = os.path.join(os.curdir, "my_logs")

def get_run_logdir():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()

log.debug("Starting logging")
img_catg = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
 
fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

print(X_train_full.shape)

def build_model(x_train):
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=x_train.shape[1:] ),
        keras.layers.Dense(300, activation="relu"),
        keras.layers.Dense(200, activation="relu"),
        keras.layers.Dense(200, activation="relu"),
        keras.layers.Dense(10, activation="softmax")
    ])
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer=keras.optimizers.SGD(lr=0.001),
                  metrics=["accuracy"])
    return model
    
tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)

history = build_model(X_train_full).fit(X_train_full,
                        y_train_full, 
                        epochs=50, 
                        validation_data=(X_test, y_test), callbacks=[tensorboard_cb])

#pd.DataFrame(history.history).plot(figsize=(8, 5))
#plt.grid(True)
#plt.gca().set_ylim(0, 1) # set the vertical range to [0-1]
#plt.show()
    
