# Amazon Prime Data Analysis & Dashboard

This project focuses on performing **Exploratory Data Analysis (EDA)** on Amazon Prime Video data and building an **interactive Streamlit dashboard**.  
It helps uncover patterns like content distribution, genre popularity, and trends in release years.

---

## **Project Overview**
- Cleaned and analyzed a dataset of Amazon Prime Video titles.
- Performed **data cleaning**: handled missing values, extracted year/month/day, and standardized data.
- Explored data to uncover:
  - Movies vs TV Shows distribution.
  - Content release trends over time.
  - Top genres, ratings, and popular keywords.
  - Advanced insights like genre co-occurrence patterns.

---

## **Features**
- **EDA Notebook** (`amazonprime_EDA.ipynb`) for detailed analysis.
- **Streamlit Dashboard** (`dashboard.py`) with:
  - Filters for type and release year.
  - Visualizations: distribution charts, genre heatmaps, word clouds, and more.
- Insights into Prime Video content trends.

---

## **Installation**
Clone the repository and set up your environment:
```bash
git clone https://github.com/Manikantareddy4567/Amazonprime-data-analysis.git
cd Amazonprime-data-analysis
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## **Running the EDA Notebook**
```bash
jupyter notebook amazonprime_EDA.ipynb
```

---

## **Running the Dashboard**
Ensure `prime_cleaned.csv` is in the same folder, then run:
```bash
streamlit run dashboard.py
```
Open the provided URL in your browser to explore the dashboard.

---

## **Repository Structure**
```
Amazonprime-data-analysis/
│-- amazonprime_EDA.ipynb       # Notebook for EDA
│-- dashboard.py                # Streamlit dashboard
│-- prime_cleaned.csv           # Cleaned dataset
│-- requirements.txt            # Dependencies
│-- README.md                   # Project documentation
```

---

## **Author**
**Manikantareddy4567**  
[GitHub Profile](https://github.com/Manikantareddy4567)
