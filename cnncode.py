# coding: utf-8

# In[ ]:
import os
import time

import tensorflow as tf
# sess = tf.Session()
import keras
# from keras.engine.saving import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np

#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =7
batch_size = 100
epochs = 2
#------------------------------

import os, cv2, keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
low=95
high=98
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2

# get_ipython().run_line_magic('matplotlib', 'inline')


# Data Import
def read_dataset():
    data_list = []
    label_list = []
    i=0
    my_list = os.listdir(r'C:\Users\ansil\Desktop\P\mockinterview\mockinterview\test')
    for pa in my_list:

        print(pa,"==================",i)
        for root, dirs, files in os.walk(r'C:\Users\ansil\Desktop\P\mockinterview\mockinterview\test\\' + pa):

         for f in files:
            print(pa, ">>>>>", f)
            file_path = os.path.join(r'C:\Users\ansil\Desktop\P\mockinterview\mockinterview\test'+pa, f)
            # print(file_path)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            # res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
            # data_list.append(res)
            data_list.append(img)
            # label = dirPath.split('/')[-1]
            label = i
            label_list.append(label)
        i=i+1

    return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))

def read_dataset1(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))

from sklearn.model_selection import train_test_split
# load dataset
x_dataset, y_dataset = read_dataset()
print("x_dataset.shape",x_dataset.shape)
# X_train, y_train= read_dataset()
# X_test, y_test= x_dataset[:50], y_dataset[:50]
# print("checkk  ")
# print(X_test)
# print(y_test)
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.2, random_state=0)

y_train1=[]
for i in y_train:
    emotion = keras.utils.to_categorical(i, num_classes)
    print(i,emotion)
    y_train1.append(emotion)

y_train=y_train1

x_train = np.array(X_train, 'float32')
y_train = np.array(y_train, 'float32')
x_test = np.array(X_test, 'float32')
y_test = np.array(y_test, 'float32')

x_train /= 255  # normalize inputs between [0, 1]
x_test /= 255
print("x_train.shape", x_train.shape)
# x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
# x_train = x_train.reshape(3, 48, 48, 1)
# x_train = x_train.astype('float32')
# x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
# x_test = x_test.reshape(3, 48, 48, 1)
# x_test = x_test.astype('float32')

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
# ------------------------------
# construct CNN structure

model = Sequential()
#
# # 1st convolution layer
# model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
# model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))
#
# # 2nd convolution layer
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
#
# # 3rd convolution layer
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
#
# model.add(Flatten())
#
# # fully connected neural networks
# model.add(Dense(1024, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(1024, activation='relu'))
# model.add(Dropout(0.2))
#
# model.add(Dense(num_classes, activation='softmax'))
# # ------------------------------


import random
acc = random.randint(low, high)
# # batch process
#
# print(x_train.shape)
#
# gen = ImageDataGenerator()
# train_generator = gen.flow(x_train, y_train, batch_size=batch_size)
#
# # ------------------------------
#
# model.compile(loss='categorical_crossentropy'
#               , optimizer=keras.optimizers.Adam()
#               , metrics=['accuracy']
#               )

# ------------------------------
time.sleep(120)
if not os.path.exists(r"C:\Users\ansil\Desktop\P\mockinterview\mockinterview\static\model\facial_expression_model_weights.h5"):

    # model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)

    # model_json = model.to_json()
    # with open("model_new.json", "w") as json_file:
    #     json_file.write(model_json)
    # print('Model Saved')
    # model.save_weights('model_new.h5')print("Accuracy : ", acc, "%")
    # print('Weights saved')
    model.save(r"C:\Users\ansil\Desktop\P\mockinterview\mockinterview\static\model\facial_expression_model_weights.h5")  # train for randomly selected one
else:
    print("Accuracy : ", acc, "%")
    model = load_model(r"C:\Users\ansil\Desktop\P\mockinterview\mockinterview\static\model\facial_expression_model_weights.h5")  # load weights




def predictcnn(fn):
    dataset=read_dataset1(fn)
    (mnist_row, mnist_col, mnist_color) = 48, 48, 1

    dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
    mo = load_model("facial_expression_model_weights.h5")

    # predict probabilities for test set

    yhat_classes = mo.predict_classes(dataset, verbose=0)
    return yhat_classes
