# 🛒 E-Commerce Revenue Leakage & Customer Intelligence System

## 📌 Project Overview

**Status:** Completed & Deployed 🚀

This project builds a **Revenue Leakage Detection and Customer Intelligence System** for an e-commerce business using real-world transactional data.

E-commerce companies often lose significant revenue due to:

* Order cancellations and returns
* Overuse of discounts
* Low repeat purchase rates
* Poor customer segmentation

This system identifies **where revenue is lost, which customers drive profit, and how to optimize business decisions** using data-driven insights.

---

## 🎯 Business Problem

Online retailers lack visibility into hidden revenue losses and customer behavior patterns.
This leads to:

* Reduced profitability
* Inefficient marketing spend
* Weak retention strategies

---

## ❓ Core Business Question

> How can we identify and reduce revenue leakage while maximizing customer lifetime value and retention?

---

## 🧠 Decision Supported

This analysis enables business stakeholders to:

* Reduce losses from cancellations and returns
* Improve customer retention strategies
* Optimize discount usage
* Focus on high-value customer segments

---

## 📊 Dataset

### 🔹 Primary Dataset

* **Brazilian E-Commerce Dataset (Olist)**
* Source: Kaggle (Raw transactional data)
* ~100,000 orders across multiple relational tables

### 🔹 Backup Datasets

* UK Online Retail II Dataset (UCI ML Repository)
* Pakistan E-Commerce Dataset (Kaggle)

### 🔹 Data Characteristics

* Multi-table relational dataset
* Contains missing values and inconsistencies
* Suitable for full ETL pipeline and statistical analysis

---

## 📁 Repository Structure

```
SectionName_TeamID_Ecommerce_Leakage_Analytics/
│
├── README.md
│
├── data/
│   ├── raw/                # Original dataset (never modified)
│   └── processed/          # Cleaned datasets
│
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
│
├── scripts/
│   └── etl_pipeline.py
│
├── tableau/
│   ├── screenshots/
│   └── dashboard_links.md
│
├── reports/
│   ├── final_report.pdf
│   └── final_presentation.pdf
│
├── docs/
│   └── data_dictionary.md
│
└── requirements.txt
```

---

## ⚙️ Tech Stack

| Tool                | Purpose                         |
| ------------------- | ------------------------------- |
| Python              | ETL, data cleaning, analysis    |
| Pandas, NumPy       | Data manipulation               |
| Matplotlib, Seaborn | Data visualization              |
| SciPy, Statsmodels  | Statistical analysis            |
| Tableau Public      | Dashboarding                    |
| GitHub              | Version control & collaboration |

---

## 🔄 Analytical Workflow

1. **Define Problem** – Revenue leakage & customer behavior
2. **Extract Data** – Load raw multi-table dataset
3. **Transform Data** – Clean, join, and engineer features
4. **Analyze Data** – EDA and statistical analysis
5. **Compute KPIs** – Business metrics and segmentation
6. **Visualize** – Interactive Tableau dashboard
7. **Recommend** – Data-driven business strategies

---

## 📈 KPI Framework

| KPI                           | Description                                 |
| ----------------------------- | ------------------------------------------- |
| Revenue Leakage Rate          | % revenue lost due to cancellations/returns |
| Customer Lifetime Value (CLV) | Total value generated per customer          |
| Repeat Purchase Rate          | % customers making multiple purchases       |
| Average Order Value (AOV)     | Avg revenue per order                       |
| RFM Segmentation              | Customer segmentation based on behavior     |
| Churn Risk Score              | Probability of customer dropping off        |
| Category Profit Margin        | Profitability by product category           |

---

## 📑 Deliverables

* ✔️ Python ETL Pipeline
* ✔️ Cleaned Dataset
* ✔️ EDA & Statistical Analysis
* ✔️ Tableau Dashboard
* ✔️ Final Report (PDF)
* ✔️ Presentation Deck (PDF)

---

## 👥 Team

| Role                         | Name           | GitHub | 
| ---------------------------- | -------------- | ------ |
| Project Lead                 | Ansh Baheti    |[techcodie](https://github.com/techcodie)| 
| Data Lead and ETL Lead       | Neha Sharma    |[Neha-Sharmaaa](https://github.com/Neha-Sharmaaa)| 
| Analysis Lead                | Tisha Kharade  |[ace-tk](https://github.com/ace-tk)| 
| Visualization Lead           | Sandesh Lendve |[mrsandy1965](https://github.com/mrsandy1965)| 
| Strategy Lead                | Sandesh Lendve |[mrsandy1965](https://github.com/mrsandy1965)| 
| PPT & Quality Lead           | Krrish Taneja  |[KT0803](https://github.com/KT0803)|

---

## 📌 Contribution Matrix

All contributions are tracked via GitHub commits and pull requests and aligned with the official contribution matrix.

---

## 📊 Business Impact

This project enables:

* Identification of hidden revenue losses
* Improved customer retention
* Better targeting of high-value customers
* Data-driven pricing and discount strategies

---

## ⚠️ Limitations & Future Scope

* Limited geographic coverage (Brazil dataset)
* No real-time data streaming
* Future scope: ML-based churn prediction & recommendation systems

---

## 📣 Final Note

This project demonstrates **end-to-end data analytics capability** — from raw data to actionable business decisions.
