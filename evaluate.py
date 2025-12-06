import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("models/drowsiness_model.h5")

# Load your test data here (same preprocessing as training)
# X_test, y_test

y_pred = model.predict(X_test)
pred = np.argmax(y_pred, axis=1)
ground = np.argmax(y_test, axis=1)

print(classification_report(ground, pred))

cm = confusion_matrix(ground, pred)
sns.heatmap(cm, annot=True, fmt='d')
plt.show()
