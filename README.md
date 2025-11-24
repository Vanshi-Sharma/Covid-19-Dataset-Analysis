# 📊 Covid-19 Data Analysis & Visualization Dashboard  

This project analyzes Covid-19 daily case trends using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.  
It includes data cleaning, feature engineering, summary statistics, and multiple visualizations to understand the spread patterns over time.

---

## 🚀 Features
- Load and preprocess Covid-19 dataset  
- Convert date column to datetime and extract:
  - Month  
  - Week number  
  - Weekday  
- Handle missing values using median imputation  
- Compute:
  - Total cases  
  - Mean, median, standard deviation  
  - Monthly case & death totals  
- Filter insights (days with high cases, high deaths, etc.)

---

## 📈 Visualizations Included

1. **Correlation Heatmap**  
   Shows relationship between daily cases, deaths, tests, and moving averages.

2. **Regression Plot**  
   Visualizes connection between daily cases and daily tests.

3. **Bar Plot**  
   Weekly distribution of daily cases with month-level comparison.

4. **KDE Plot**  
   Distribution of daily deaths for each month.

These plots help reveal patterns, trends, and dependencies in the Covid-19 data.

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## 📁 Dataset
A small custom dataset (under 50 rows) is used for simpler, faster analysis and visualization.

Columns include:  
`Date`, `Daily_Cases`, `Daily_Deaths`, `Daily_Tests`, `7Day_MA_Cases`, `Month`, `Week`, `Weekday`

---
