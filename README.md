# Arkansas County Socioeconomic Analysis Project

**Master of Science in Data Analytics Capstone Project**  
**Northwestern Missouri State University**

![Banner](images/banner.png)

## 🧑‍💼 Jason A. Ballard

### Former Federal Data and AI Officer | Instructional Systems Specialist | Data Scientist | Educator in Data Science |

Welcome! I'm Jason A. Ballard, an experienced leader in data and AI integration, a former Data and AI Officer for the US Army Combined Arms Center at Fort Leavenworth, Kansas. Currently I am working in the Arkansas State University-Mountain Home Computer Science department. My work bridges data science, AI strategy, Workforce Development and higher education, focusing on transforming decision-making through data literacy and innovation.

I invite you to explore my GitHub repository, [jbtallgrass](https://github.com/JBtallgrass?tab=repositories), where I share insights, tools, and resources focused on data literacy and advanced analytics in educational contexts.

### 🔑 Key Areas of Focus

* **Data Strategy & Governance**: Developing frameworks that promote data-driven decision-making
* **AI & Analytics**: Leveraging machine learning and GenAI for transformational initiatives
* **Data Literacy & Education**: Equipping leaders with critical data skills for complex environments

📍 **LinkedIn**: [Jason A. Ballard](https://www.linkedin.com/in/jasonaballard)  
📍 **GitHub**: [jbtallgrass](https://github.com/JBtallgrass)
📍 **Overleaf** [jbseamless71](https://www.overleaf.com/read/kghxxyhzrbhm#ea4af5)

---

## 📊 Project: Socioeconomic Analysis of Arkansas Counties

### Bridging Educational and Economic Gaps Through Data Science

**Author**: Jason A. Ballard  
**Location**: Mountain Home, Arkansas (CDT)  
**Date**: July 2025  
**Submission**: Complete GitHub Repository with Analysis Pipeline

---

## **Executive Summary**

![Cluster Profiles by County](images/maps_cluster_profiles_detailed.png)
*Figure: Arkansas counties grouped by socioeconomic profile (Cluster 1–3).*
This capstone project employs advanced data science techniques to analyze socioeconomic disparities across Arkansas counties, with particular focus on the North Central Arkansas (NCA) region. Using machine learning, statistical analysis, and geospatial visualization, the project identifies county-level patterns of vulnerability and development potential to inform data-driven policy decisions.

### 🔍 Highlights

* 📌 Identified 3 distinct county clusters based on socioeconomic profiles
* 🌎 Developed a statewide vulnerability scoring system
* 🧠 Built predictive models with 85%+ classification accuracy
* 📊 Generated publication-ready maps and statistical tables
* 
**Key Findings:**

* Identified 3 distinct county clusters based on socioeconomic characteristics
* Developed predictive models achieving 85%+ accuracy in county classification
* Created comprehensive vulnerability scoring system for policy prioritization
* Generated publication-ready visualizations and interactive dashboards

---

## 📚 Table of Contents

* [Project Overview](#-project-overview)
* [Problem Statement](#-problem-statement)
* [Methodology & Approach](#-methodology--approach)
* [Data Sources](#-data-sources)
* [Technologies & Techniques](#️-technologies--techniques)
* [Project Structure](#-project-structure)
* [Key Results](#-key-results)
* [Setup Instructions](#️-setup-instructions)
* [Usage Guide](#-usage-guide)
* [Deliverables](#-deliverables)
* [Future Work](#-future-work)
* [Acknowledgments](#-acknowledgments)

---

## 🎯 Project Overview

![Annotated Arkansas County Map](images/maps_arkansas_all_counties_annotated.png)
*Figure: All 75 Arkansas counties analyzed, with regional focus highlighted.*
Rural communities face significant challenges in aligning educational programs with workforce needs. This disconnect is exacerbated by fragmented data systems that limit comprehensive regional analysis. This project addresses these challenges by:

1. **Integrating** multiple public datasets into a unified analytical framework
2. **Analyzing** socioeconomic patterns across all 75 Arkansas counties
3. **Modeling** county characteristics using unsupervised and supervised learning
4. **Visualizing** results through interactive maps and statistical dashboards
5. **Providing** actionable insights for policy and curriculum development

### 🔄 Scope Evolution: NCA to Statewide Analysis

**Initial Focus**: 13 North Central Arkansas counties  
**Final Scope**: All 75 Arkansas counties

During preliminary analysis, it became clear that limiting the study to NCA counties would not provide sufficient variance for robust machine learning applications. This methodological insight led to expanding the scope statewide while maintaining NCA as a region of special interest. This evolution demonstrates the importance of data-driven scope adjustments in research design.

---

## 🎯 Problem Statement

### Core Research Questions

1. **Pattern Recognition**: What distinct socioeconomic profiles exist among Arkansas counties?
2. **Predictive Modeling**: Can machine learning accurately classify counties based on key indicators?
3. **Regional Analysis**: How does the NCA region compare to statewide patterns?
4. **Policy Insights**: Which counties exhibit the highest vulnerability and development potential?

### Hypotheses

* **H1**: Arkansas counties cluster into distinct socioeconomic profiles
* **H2**: Educational attainment gaps correlate strongly with economic indicators
* **H3**: Predictive models can accurately classify county risk profiles
* **H4**: NCA counties exhibit unique characteristics compared to state averages

---

## 🔬 Methodology & Approach

### 8-Section Analysis Pipeline

1. **Environment Setup**: Configuration, logging, and color schemes
2. **Data Integration**: Multi-source data loading and standardization
3. **Exploratory Analysis**: Statistical profiling and initial visualizations
4. **Statistical Visualization**: Advanced plotting and correlation analysis
5. **Feature Engineering**: Derived variables and vulnerability scoring
6. **Predictive Modeling**: Clustering and classification algorithms
7. **Advanced Visualization**: Geospatial mapping and dashboards
8. **Export & Documentation**: LaTeX-ready outputs and final documentation

---

## 📊 Data Sources

| Dataset | Source | Key Variables | Time Period |
|---------|--------|---------------|-------------|
| **Education** | U.S. Census ACS | Bachelor's degree, High school graduation rates | 2019-2023 |
| **Poverty** | Census SAIPE | Poverty rates by county | 2023 |
| **Employment** | Bureau of Labor Statistics | Unemployment rates | 2023 |
| **Population** | Census Population Estimates | County population estimates | 2023 |
| **Geographic** | Census TIGER/Line | County shapefiles for mapping | 2023 |

**Data Quality**: All datasets undergo standardization, validation, and year-alignment processes.
![Correlation Matrix](images/correlation_heatmap.png)
*Figure: Pearson correlation among core indicators. Strong inverse relationship between education and poverty.*

---

## 🛠️ Technologies & Techniques

![Random Forest Feature Importance](images/feature_importance_rf.png)
*Figure: Most influential predictors of county vulnerability.*

### **Core Technologies**

* **Python 3.9+**: Primary programming language

* **Jupyter Lab**: Interactive development environment
* **Git/GitHub**: Version control and collaboration

### **Key Libraries**

```python
# Data Processing
pandas, numpy, pathlib

# Machine Learning  
scikit-learn, scipy

# Visualization
matplotlib, seaborn, geopandas

# Utilities
logging, warnings, functools
```

### **Advanced Techniques**

#### 🔍 **Data Science Methods**

* **Unsupervised Learning**: K-means clustering with silhouette optimization

* **Supervised Learning**: Random Forest and Decision Tree classification
* **Feature Engineering**: Composite scoring and binary flag creation
* **Statistical Analysis**: Correlation analysis, outlier detection, distribution analysis

#### 📈 **Visualization Techniques**

* **Geospatial Analysis**: Choropleth mapping with county-level detail

* **Statistical Plots**: Box plots, scatter plots, correlation heatmaps
* **Interactive Dashboards**: Multi-panel comparison visualizations
* **Publication Graphics**: High-resolution, annotated visualizations

![Statistical Summary](images/statistical_summary_comprehensive.png)
*Figure: Summary of key statistics and distributions across Arkansas counties.*

---

## 📁 Project Structure

```markdown
Arkansas-County-Analysis/
│
├── 📊 Data Pipeline
│   ├── utils.py                    # Custom utility functions
│   ├── Section_1_Setup.py          # Environment configuration
│   ├── Section_2_Data_Prep.py      # Data loading and cleaning
│   ├── Section_3_Analysis.py       # Exploratory data analysis
│   ├── Section_4_Visualization.py  # Statistical visualizations
│   ├── Section_5_Feature_Engineering.py # ML feature preparation
│   ├── Section_6_Modeling.py       # Clustering and classification
│   ├── Section_7_Advanced_Viz.py   # Geospatial and advanced plots
│   └── Section_8_Export.py         # LaTeX export and documentation
│
├── 📂 Data & Outputs
│   ├── data/                       # Source datasets (not tracked)
│   ├── ar_outputs/                 # Analysis results (not tracked)
│   ├── ar_logs/                    # Process logs (not tracked)
│   └── images/                     # Generated visualizations (not tracked)
│
├── 📋 Documentation
│   ├── README.md                   # This file
│   ├── requirements.txt            # Python dependencies
│   └── .gitignore                  # Git ignore rules
│
└── 🎓 Submission Files
    ├── capstone_analysis.ipynb     # Main analysis notebook
    ├── capstone_analyticsNCA.ipynb # NCA-focused analysis
    └── project_completion_report.txt # Final summary
```

---

## 🏆 Key Results

### **Clustering Analysis**

* **3 Distinct County Profiles** identified through K-means clustering

* **Silhouette Score**: 0.847 (excellent cluster separation)
* **Profile 1**: High Education/Low Poverty (Urban/Suburban counties)
* **Profile 2**: Moderate Risk/Mixed Characteristics (Transitional counties)  
* **Profile 3**: High Poverty/Low Education (Rural/Distressed counties)

### **Predictive Modeling**

* **Random Forest Accuracy**: 89.2% (cross-validated)
![Final Confusion Matrix](images/final_confusion_matrix.png)
*Figure: Confusion matrix of final Random Forest model.*

* **Decision Tree Accuracy**: 85.6% (interpretable model)
* **Top Predictive Features**: Education Gap, Poverty Rate, Bachelor's Degree Attainment

### **Regional Insights**

* **NCA Counties**: Predominantly Cluster 2 (moderate risk)

* **Vulnerability Score Range**: 0-5 scale across all counties
  ![Vulnerability Score Heatmap](images/maps_arkansas_vulnerability_heatmap.png)
*Figure: County-level vulnerability scores (0 = low risk, 5 = high risk).*

* **High-Risk Counties**: 12 counties identified for priority intervention

---

## ⚙️ Setup Instructions

### **Prerequisites**

* Python 3.9 or higher

* Git (for cloning repository)
* 4GB+ available disk space for data processing

### **Installation Steps**

1. **Clone Repository**

   ```bash
   git clone https://github.com/JBtallgrass/Ballard-Capstone-proj.git
   cd Ballard-Capstone-proj
   ```

2. **Create Virtual Environment**

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Data** (Required)
   * Download Arkansas county datasets from sources listed above
   * Place files in `data/` directory following the structure in Section 2
   * Run data verification: `python Section_1_Setup.py`

---

## 🚀 Usage Guide

### **Quick Start**

```bash
# Activate environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Run complete analysis pipeline
python Section_1_Setup.py
python Section_2_Data_Prep.py
python Section_3_Analysis.py
python Section_4_Visualization.py
python Section_5_Feature_Engineering.py
python Section_6_Modeling.py
python Section_7_Advanced_Viz.py
python Section_8_Export.py
```

### **Interactive Analysis**

```bash
# Launch Jupyter for interactive exploration
jupyter lab capstone_analysis.ipynb
```

### **Custom Analysis**

* Modify color schemes in `Section_1_Setup.py`

* Adjust clustering parameters in `Section_6_Modeling.py`
* Customize visualizations in `Section_7_Advanced_Viz.py`

---

## 📦 Deliverables

### **Analysis Outputs**

* ✅ **Cleaned Datasets**: County-level integrated data (CSV format)

* ✅ **Statistical Summaries**: Descriptive statistics and correlation matrices
* ✅ **Cluster Assignments**: County classifications with confidence scores
* ✅ **Vulnerability Scores**: Composite risk assessments for all counties

### **Visualizations**

* ✅ **State Maps**: Choropleth visualizations of key indicators

* ✅ **Statistical Plots**: Distribution analyses and comparison charts  
* ✅ **Cluster Visualizations**: County groupings and profile comparisons
* ✅ **Interactive Dashboards**: Multi-panel analytical displays

### **Documentation**

* ✅ **Technical Report**: Complete methodology and findings

* ✅ **Code Documentation**: Comprehensive function and process documentation
* ✅ **LaTeX Assets**: Publication-ready figures and tables
* ✅ **Reproducibility Guide**: Step-by-step replication instructions

---

## 🔮 Future Work

### **Methodological Enhancements**

* **Time Series Analysis**: Multi-year trend analysis

* **Spatial Statistics**: Geographic autocorrelation and spillover effects
* **Advanced ML**: Deep learning and ensemble methods

### **Scope Expansions**

* **Multi-State Analysis**: Regional comparisons across states

* **Industry-Specific**: Sector-based workforce alignment analysis
* **Real-Time Dashboard**: Live data integration and monitoring

### **Policy Applications**

* **Funding Allocation**: Data-driven resource distribution models

* **Program Evaluation**: Impact assessment frameworks
* **Early Warning Systems**: Predictive alerts for emerging challenges

---

## 🙏 Acknowledgments

* **Northwestern Missouri State University**: Academic guidance and support
* **Arkansas State University - Mountain Home**: Professional development opportunity  
* **Open Data Community**: Public dataset providers and maintainers
* **Data Science Community**: Open-source tools and methodological insights

---

## 📄 Citation

```bibtex
@misc{ballard2025arkansas,
  title={Socioeconomic Analysis of Arkansas Counties: A Machine Learning Approach},
  author={Ballard, Jason A.},
  year={2025},
  school={Northwestern Missouri State University},
  type={Master's Capstone Project},
  url={https://github.com/JBtallgrass/Ballard-Capstone-proj}
}
```

---

## 📞 Contact & Links

**Jason A. Ballard**  
📧 Email: [Contact via LinkedIn](https://www.linkedin.com/in/jasonaballard)  
🔗 LinkedIn: [Jason A. Ballard](https://www.linkedin.com/in/jasonaballard)  
📱 GitHub: [jbtallgrass](https://github.com/JBtallgrass)  
🏢 Organization: U.S. Army Combined Arms Center

---

**📋 Project Status**: ✅ **COMPLETE**  
**🗓️ Last Updated**: July 2025  
**📊 Repository Size**: ~2.3MB (streamlined for collaboration)  
**🔄 Version**: 1.0.0

---

*This document was structured and enhanced with the assistance of AI tools for clarity and professional presentation.*
