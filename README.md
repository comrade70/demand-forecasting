# Demand Forecasting with Machine Learning

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EC6B23?style=for-the-badge&logo=xgboost&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

Demand forecasting is an important task in the supply chain and retail industries as it helps organisations optimise inventory. This project explores machine learning techniques to help organisations make accurate demand predictions.

![Demand Forecasting App](images/app.JPG)

## Project Overview

This repository is an implementation of a demand forecasting pipeline that includes

- Data exploration and visualisation
- Data preprocessing and feature engineering
- Model development using machine learning
- Model evaluation using performance metrics
- Deployment through Streamlit, a web-based interactive application 

## Key Features

- Exploratory Data Analysis (EDA)  
- Data preprocessing and feature engineering  
- Machine learning model training  
- Model evaluation 
- Interactive prediction interface using Streamlit  

## Dataset

The dataset contains historical sales data, including features that influence product demand, such as:

`Date`, `Store ID`, `Product ID`, `Category`, `Region`,
`Inventory Level`, `Units Sold`, `Units Ordered`, `Price`, `Discount`,
`Weather Condition`, `Promotion`, `Competitor Pricing`, `Seasonality`,
`Epidemic`, `Demand`

## Machine Learning Model

The primary model used in this project is `XGBoost Regressor`, a powerful gradient boosting algorithm popularly used for predictive modelling.

## Streamlit Application

The repository includes a `Streamlit`, an interactive web based dashboard that allows users to generate demand predictions.

Features:

- Input feature
- View predicted demand

## Tools

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost
- Streamlit

## Installation

- Clone the repository
```bash
git clone https://github.com/comrade70/demand-forecasting.git
```

```bash
cd demand-forecasting
```

- Run the application locally

```bash
streamlit run app.py
```

## License

This project is licensed under the MIT License.

---

If you find this project useful, please consider starring ⭐ the repository.
