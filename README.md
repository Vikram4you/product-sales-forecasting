## 🛒 Product Sales Forecasting – End-to-End Product Sales Forecasting project

## 📌 Problem Statement

In the competitive retail industry, the ability to accurately forecast future product sales is critical for operational efficiency and strategic decision-making.  
This project aims to build a predictive model that can forecast daily sales for retail stores using historical data and features such as store characteristics, promotions, and temporal patterns (holidays, seasonality, etc.).

---

## 🎯 Business Objectives

- Improve **inventory planning** to reduce stockouts and over-stocking.
- Support **resource planning** and **budget allocation**.
- Quantify the **impact of discounts and holidays** on sales.
- Provide a **deployment-ready solution** that can be integrated into business systems for real-time prediction.

---

## 📂 Dataset Overview

| Column          | Description |
|----------------|-------------|
| `ID`            | Unique identifier for each record |
| `Store_id`      | Unique store identifier |
| `Store_Type`    | Type of store (S1, S2, S3, etc) |
| `Location_Type` | Urban, suburban, etc |
| `Region_Code`   | Geographical region |
| `Date`          | Date of observation |
| `Holiday`       | Whether the date is a holiday (1/0) |
| `Discount`      | Whether a discount was applied (Yes/No) |
| `#Order`        | Number of orders on that day |
| `Sales`         | Total sales amount |

---

## 🔎 Exploratory Data Analysis (EDA) & Hypothesis Testing

**Key insights:**

| Hypothesis | Result |
|-----------|--------|
| Discounts lead to higher sales | ✅ *Significant* |
| Holiday sales > regular day sales | ✅ *Significant* |
| Sales vary significantly between store types | ✅ |
| Sales vary significantly across regions | ✅ |
| `#Order` is strongly correlated with `Sales` | ✅ ρ = 0.94 |

These results clearly indicate that **discounts, holidays, store type, and region are key drivers** of sales and should be included in the predictive model.

---

## ⚙️ Feature Engineering

- Converted `Date` into date parts → `year`, `month`, `day_of_week`, `is_weekend`
- Encoded categorical variables
- Created **lag features**: previous 1-day and 7-day sales
- Added **rolling window statistics** (7-day mean & std)

---

## 🤖 Model Development

| Model | Notes |
|------|----------------------|
| Baseline (Naïve) | Previous day’s sales |
| XGBoost Regressor ✅ *(Final)* | Captured non-linear behavior and temporal dependencies |

**Performance on Test Set:**

| Metric | Score |
|--------|-----------|
| MAE    | 2139.94   |
| RMSE   | 3172.99   |

The **forecast closely follows the actual sales trend**, demonstrating strong generalization on unseen data.

---

## 🚀 Deployment

The final model was **serialized** using `pickle` and deployed using a **Flask API**.

| Endpoint | Method | Description |
|---------|--------|------------|
| `/predict` | POST | Returns predicted sales for input features |

Example request:
```json
POST /predict
{
  "Store_id":1,
  "Store_Type":0,
  "Location_Type":2,
  "Region_Code":1,
  "Holiday":0,
  "Discount":1,
  "#Order":25,
  "year":2019,
  "month":5,
  "day_of_week":2,
  "is_weekend":0,
  "lag_1":5000,
  "lag_7":4800,
  "rolling_mean_7":5150,
  "rolling_std_7":320
}
```

---

## 📊 Tableau Dashboard – What to Build

**1. Sales Performance Dashboard**
- Line chart: daily / monthly sales trend
- Bar chart: sales by *store type*
- Bar chart: sales by *location type*

**2. Regional Sales Dashboard**
- Heatmap: region vs month with sales value
- KPI card: total sales per region

**3. Promotion & Holiday Impact**
- Boxplot: sales on discount vs non-discount days
- Bar chart: average sales on holidays vs non-holidays

**4. Forecast Monitoring Dashboard**
- Line chart showing **Actual vs Predicted** sales
- Filter controls: store type, region, date range, holiday flag

---

## ✅ Next Steps

- Publish the Tableau dashboard on Tableau Public ✅  
- Publish this repo with the notebook + `app.py` ✅  
- Write and post the accompanying technical blog  
- Record Loom demo video

---

### 💡 Author  
*VIKRAM — Data Science Portfolio Project*
