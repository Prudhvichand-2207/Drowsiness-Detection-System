import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array

model = tf.keras.models.load_model("models/drowsiness_model.h5")

img = cv2.imread("sample.jpg")
img = cv2.resize(img, (150,150))
img = img / 255.0
img = np.reshape(img, (1,150,150,3))

pred = model.predict(img)
label = np.argmax(pred)

if label == 0:
    print("Drowsy Detected")
else:
    print("Normal")
