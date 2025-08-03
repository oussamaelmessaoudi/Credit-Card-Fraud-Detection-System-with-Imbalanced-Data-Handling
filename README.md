# 🕵️‍♂️ Fraud Detection with Logistic Regression

This project focuses on detecting fraudulent transactions using machine learning. It leverages **Logistic Regression** as a baseline model and applies **SMOTE** to handle class imbalance, ensuring better fraud detection performance.

---

## 📦 Project Overview

- **Goal**: Identify fraudulent transactions in a highly imbalanced dataset.
- **Model**: Logistic Regression
- **Techniques Used**:
  - Data preprocessing
  - SMOTE (Synthetic Minority Over-sampling Technique)
  - Model training and evaluation
  - Confusion matrix and classification metrics

---

## 🧠 Dataset

- The dataset contains transaction records labeled as:
  - `0`: Non-fraudulent
  - `1`: Fraudulent
- Highly imbalanced: Fraud cases are rare compared to non-fraud.

---

## ⚙️ Technologies

- Python
- scikit-learn
- imbalanced-learn
- pandas, numpy
- matplotlib / seaborn (optional for visualization)

---

## 🚀 Workflow

<p align="center">
  <img src="assets/diagram-Workflow/Credit%20Card%20Fraud%20Detection%20Workflow.svg" alt="Workflow Diagram" />
</p>

1. **Data Preprocessing**
   - Feature selection and scaling
   - Train-test split

2. **Balancing the Training Set**
   - Applied SMOTE to oversample the minority class

3. **Model Training**
   - Trained Logistic Regression on the balanced dataset

4. **Evaluation**
   - Confusion matrix
   - Classification report
   - Accuracy, precision, recall, F1-score


---

## 📊 Results

### Confusion Matrix

[[55406 1458] [ 8 90]]


### Classification Report

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0 (Non-Fraud) | 1.00 | 0.97 | 0.99 | 56864 |
| 1 (Fraud)     | 0.06 | 0.92 | 0.11 | 98 |

- **Accuracy**: 97.4%
- **High recall for fraud**: 92% of fraud cases detected
- **Low precision for fraud**: Many false positives

---

## 🧪 Author

**Oussama**  
Passionate about building scalable systems, solving technical challenges, and exploring data-driven solutions.

---

## 📬 Contact

Feel free to reach out or contribute to the project!

