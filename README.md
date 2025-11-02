# 📊 Customer Segmentation at LG Corporation

**Author:** Osazuwa Stanley Omoregbe  
**Course:** Business Analytics Final Project – Nexford University  
**Deployment:** 🌍 [Live on Render](https://lg-final-projects.onrender.com)  
_(AWS deployment attempt unsuccessful, so Render was used for hosting)_

---

## 🔑 Executive Summary

This project applies **data-driven customer segmentation** to LG Corporation’s customer base, using clustering techniques to uncover distinct behavioral groups. By analyzing **age, annual income, and spending score**, the model identifies high-value customers, disengaged segments, and premium buyers. The insights enable LG to **personalize marketing strategies, improve retention, and maximize ROI**. The solution is deployed as an **interactive dashboard** on Render, making the analysis accessible and actionable.

---

## 📌 Project Overview

This project is the **Final Business Analytics Project** for Nexford University.  
The objective is to analyze LG Corporation’s customer data to identify **distinct customer segments** and provide insights that can guide **targeted marketing strategies**.

The project demonstrates:

- Data preprocessing and exploratory data analysis (EDA)
- Customer segmentation using **KMeans clustering**
- Evaluation of cluster quality using **Elbow** and **Silhouette** methods
- Deployment of an interactive **Flask web application** for visualization
- Clear business implications for LG’s marketing strategy

---

## 🎯 Business Problem

LG Corporation recognized the need for a robust analytics model to:

- Better understand customer behavior
- Identify distinct customer groups
- Tailor marketing strategies for each segment

**Objective:**

> To analyze customer data, identify meaningful clusters, and provide actionable insights for marketing optimization.

---

## 🛠️ Methodology

1. **Data Preparation**

   - Dataset: `lg_customer_data.csv`
   - Features used: `Age`, `Annual_Income`, `Spending_Score`
   - Standardization applied using `StandardScaler`

2. **Exploratory Data Analysis (EDA)**

   - Distribution plots for Age, Income, and Spending
   - Correlation heatmaps
   - Scatter plots for feature relationships

3. **Clustering**

   - Algorithm: **KMeans**
   - Optimal number of clusters determined using:
     - Elbow Method
     - Silhouette Score
   - Final segmentation visualized in 2D scatter plots

4. **Deployment**
   - Flask app built with interactive dashboard
   - Users can select number of clusters dynamically
   - Cluster summary table generated and downloadable as CSV
   - Deployed on **Render** (AWS attempt unsuccessful)

---

## 📊 Results & Visualizations

### 1. Customer Segments

![Customer Segments](https://lg-final-projects.onrender.com/plots/segments_plot.png)

This scatter plot shows customer clusters based on **Annual Income** and **Spending Score**. Each color represents a distinct segment.

---

### 2. Clustering Evaluation

![Clustering Evaluation](https://lg-final-projects.onrender.com/plots/clustering_eval.png)

- **Elbow Method**: Helps determine the optimal number of clusters.
- **Silhouette Score**: Measures cluster quality and separation.

---

### 3. Cluster Summary

![Cluster Summary](https://lg-final-projects.onrender.com/plots/cluster_summary.png)

- ✅ **Green** → Highest Income Cluster
- 🔴 **Red** → Lowest Spending Cluster
- 🔵 **Blue** → Highest Spending Cluster

---

## 🚀 Deployment

- **Live App:** [Customer Segmentation Dashboard](https://lg-final-projects.onrender.com)
- **GitHub Repository:** [GitHub Repo Link](https://github.com/yourusername/lg-customer-segmentation)

---

## ⚙️ Tech Stack

- **Language:** Python 3.12+
- **Framework:** Flask
- **Libraries:**
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
- **Deployment:** Render (Gunicorn + Flask)

---

## ▶️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lg-customer-segmentation.git
   cd lg-customer-segmentation
   ```
