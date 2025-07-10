# Ballard Capstone Project

The project supports the final requirements necessary to complete the Master of Science in Data Analytics from Northwest Missouri State University

![Banner](images/banner.png)

## 🧑‍💼 Jason A. Ballard

### Instructional Systems Specialist | Data Scientist | Data and AI Officer | Data Literacy Advocate | Educator in Professional Military Education

Welcome! I'm Jason A. Ballard, an experienced leader in data and AI integration, currently serving as the Data and AI Officer for the US Army Combined Arms Center at Fort Leavenworth, Kansas. My work bridges data science, AI strategy, and higher education, focusing on transforming decision-making through data literacy and innovation.

I invite you to explore my GitHub repository, [jbtallgrass](https://github.com/JBtallgrass?tab=repositories), where I share insights, tools, and resources focused on data literacy and advanced analytics in educational contexts. My projects emphasize practical solutions, open collaboration, and a commitment to enhancing data accessibility across teams.

### 🔑 Key Areas of Focus

* **Data Strategy & Governance**: Developing frameworks that promote data-driven decision-making and cross-departmental data sharing.
* **AI & Analytics**: Leveraging data analytics and GenAI to unlock insights and drive transformational initiatives within the Army University.
* **Data Literacy & Education**: Equipping leaders and students with data literacy skills critical for today's complex, data-rich environments.

📍 **LinkedIn**: [Jason A. Ballard](https://www.linkedin.com/in/jasonaballard)
📍 **GitHub**: [jbtallgrass](https://github.com/JBtallgrass)

---

## Capstone Project: Bridging the Gap in North Central Arkansas

### Jason Ballard

#### Mountain Home, Arkansas (CDT)

#### July 2025

> 📁 Submission: GitHub Repository with Jupyter Notebook and Final Project Files

---

## **TL;DR:**

This capstone project explores the alignment between education and employment needs across North Central Arkansas counties using publicly available data. The goal is to uncover patterns of vulnerability and development potential through exploratory data analysis, feature engineering, and predictive modeling. The project supports data-informed local policy, workforce planning, and curriculum development.

---

## 📚 Table of Contents

* [Project Overview](#project-overview)
* [Problem Statement](#problem-statement)
* [Project Goals](#project-goals)
* [Data Sources](#data-sources)
* [Technologies Used](#technologies-used)
* [Techniques Used](#techniques-used)
* [Project Structure](#project-structure)
* [Final Overview: Full Data Pipeline](#final-overview-full-data-pipeline)
* [Submission Checklist](#submission-checklist)
* [Links](#links)

---

## Project Overview

Rural communities often struggle to align education programs with workforce needs. This disconnect is compounded by siloed data systems that make it difficult to assess county-level trends across education, poverty, and employment. This capstone uses publicly available datasets to assess economic vulnerability and educational gaps across North Central Arkansas counties, with the aim of informing policy and curriculum development at the local level.

---

## Problem Statement

Although extensive public data exist on poverty, educational attainment, unemployment, and population, these indicators are frequently stored in siloed systems and analyzed independently. This fragmentation limits the ability of public institutions—particularly in rural regions—to conduct integrated, county-level assessments of regional need.

### Core Questions

1. **Pattern Identification**: Can we identify meaningful disparities in educational and economic conditions across counties in North Central Arkansas?
2. **Predictive Insight**: Can machine learning models classify counties based on shared vulnerabilities or developmental potential?

---

## Project Goals

* Build a consolidated, clean, and enriched dataset for Arkansas counties
* Conduct exploratory analysis and visualize disparities
* Engineer features to reflect economic and educational risk
* Apply clustering and classification models to identify county profiles
* Produce interpretable visual and tabular outputs to support decision-making

---

## Data Sources

* **Education**: U.S. Census Bureau American Community Survey
* **Poverty**: U.S. Census Small Area Income and Poverty Estimates (SAIPE)
* **Unemployment**: Bureau of Labor Statistics / Local Area Unemployment Statistics
* **Population Estimates**: U.S. Census Population Estimates Program
* **Crosswalks**: 2010 to 2020 FIPS code transitions

---

## Technologies Used

* **Python** (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
* **Jupyter Notebook**
* **Pathlib, Logging, Regex** for scripting and logging
* **Git & GitHub** for version control and sharing

---

## Techniques Used

### 💡 Data Preparation & Preprocessing

* Multi-source data integration (education, poverty, unemployment, population)
* Standardization of county names and FIPS codes
* Attribute year filtering and crosswalking
* Data normalization using MinMaxScaler
* Derived variables (e.g., Education Gap, % with Bachelor's degree)

### 🔢 Exploratory Data Analysis (EDA)

* Descriptive statistics, outlier detection, and range comparisons
* Dot plots, boxplots with annotations, correlation heatmaps, and pair plots
* Narrative summary generation for each variable

### 🔄 Feature Engineering

* Creation of binary risk flags based on thresholds (e.g., High Poverty)
* Construction of composite vulnerability scores
* Normalization of all indicator variables

### 🧬 Clustering & Classification

* **K-Means Clustering** to identify 3 distinct county profiles
* **Random Forest Classifier** to predict cluster membership
* **Decision Tree** to visualize prediction logic
* Model evaluation using silhouette scores, accuracy, and confusion matrices

### 🔧 Project Structure & Automation

* Section-based Jupyter Notebook layout
* Modular utility functions (`utils.py`)
* Logging system to track processing and outputs
* Auto-generated visualizations and CSV outputs

---

## Project Structure

```plaintext
├── data/                          # Source datasets
├── images/                        # Banner and plots
├── ar_outputs/                    # Output data and logs
├── utils.py                       # Custom utility functions
├── capstone-analysis.ipynb        # Main notebook
├── README.md                      # This file
```

---

## Final Overview: Full Data Pipeline

1. **Setup & Configuration**: Import libraries, configure logging, establish file paths
2. **Load Data**: Read and standardize multiple datasets
3. **Merge & Clean**: Combine county-level data and filter for Arkansas
4. **EDA**: Explore and visualize distributions, outliers, and correlations
5. **Feature Engineering**: Create derived fields, binary risk flags, and vulnerability scores
6. **Clustering**: Use K-Means to define county groupings
7. **Classification**: Train Random Forest and Decision Tree to predict clusters
8. **Interpretation**: Summarize results, visualize groupings, and export tables

---

## Submission Checklist

* [x] Capstone Jupyter Notebook: `capstone-analysis.ipynb`
* [x] Final README: `README.md`
* [x] Supporting files and data exports
* [x] Visuals, feature importances, and model evaluations

---

## Links

* 📘 [Notebook Preview](capstone_analysisvAR.ipynb)
* 📘 [NorthCentral Arkansas Notebook Preview](capstone_analyticsNCA.ipynb)
* 📝 [GitHub Repository](https://github.com/JBtallgrass)

---

🌟 Document completed by Jason A. Ballard
🌟 A GenAI assistant platform was used to structure and edit this document.
