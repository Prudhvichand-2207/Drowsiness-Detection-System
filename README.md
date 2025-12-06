# Drowsiness-Detection-System

A Deep Learning–based **Drowsiness Detection System** that automatically identifies whether a person is **Drowsy or Normal** using images. The system is built using **Transfer Learning (MobileNet)** and achieves high accuracy with real-time prediction support.

---

## 📌 Project Overview

Driver drowsiness is one of the major causes of road accidents. This project uses a **Convolutional Neural Network (CNN)** based on **MobileNet architecture** to classify eye-state / face images into:

- **Drowsy**
- **Normal**

The model is trained using image augmentation and evaluated using multiple performance metrics such as **Accuracy, Confusion Matrix, F1-score, and ROC-AUC curve**.

---

## Features

Image Preprocessing & Normalization  
Data Augmentation  
Transfer Learning with MobileNet  
Training & Evaluation Pipeline  
Confusion Matrix Visualization  
ROC Curve & AUC Score  
Real-Time Image Prediction Support  
Clean Modular Code Structure  

---

## Technologies Used

- **Python**
- **TensorFlow 2.10 & Keras**
- **OpenCV**
- **NumPy & Pandas**
- **Matplotlib & Seaborn**
- **Scikit-Learn**
- **Scikit-Image**
- **TQDM**

---

## Model Architecture

- **Base Model: MobileNet (Pre-trained on ImageNet)**
- **Input Shape: 150 × 150 × 3**
- **Hidden Layer: Dense (128 neurons, ReLU)**
- **Output Layer: Dense (2 neurons, Sigmoid)**
- **Loss Function: Categorical Crossentropy**

---

## Performance Metrics

- **Accuracy**
- **Precision**
- **Recall (Sensitivity)**
- **Specificity**
- **F1 Score**
- **Confusion Matrix**
- **ROC Curve & AUC Score**

---

## Applications

- **Driver Drowsiness Detection**
- **Medical Monitoring**
- **Industrial Safety**
- **Surveillance & Security Systems**

---
## Author

- Prudhvichand
- B.tech-computer Science

