# Diabetes-Prediction

This project aims to predict the chance of diabetes of a person.

The dataset is taken from [Kaggle](https://www.kaggle.com/ishandutta/early-stage-diabetes-risk-prediction-dataset).

### How to run the app?

- **Clone the project:** 
  `git clone git@github.com:SHAIMA-HAQUE/Diabetes-Prediction.git`
- **Install streamlit:**
  `pip install streamlit`
- **Run the app:**
  `streamlit run app.py`

The dataset contains features:
- Age
- Gender
- Polyuria
- Polydipsia
- Sudden weight loss
- Weakness
- Polyphagia
- Genital thrush
- Visual Blurring
- Itching
- Irritability
- Delayed Healing
- Partial Paresis
- Muscle Stiffness
- Alopecia
- Obesity

**The correlation between the features and diabetes was found to be :**

![Correlation with diabetes](https://github.com/SHAIMA-HAQUE/Diabetes-Prediction/blob/main/Correlation%20with%20diabetes.png)

**So,the final features chosen are :**

- Age
- Polyuria
- Polydipsia
- Gender
- Partial Paresis
- Sudden Weight Loss
- Irritability
- Delayed Healing
- Alopecia
- Itching

### After using Random Forest Classifier the model gives an accuracy of 98.72%

The app predicts if there is a chance of diabetes or not and then suggests some remedies for the same.

## This app is built for experiment sake, any prediction made is based off the dataset only. Please, consult a doctor if not sure. 
