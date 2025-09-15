# Airbnb London – Data Wrangling & EDA
End‑to‑end exploratory data analysis (EDA) and data cleaning project focused on **short‑term rental pricing in London**. This repo is designed to showcase **data wrangling, feature engineering, visualization, and storytelling**.

> **Goal:** Understand what drives listing prices in London and produce actionable insights with clean visuals and a polished narrative.

---

## 📦 Repository Structure
```
airbnb-london-eda/
├─ README.md
├─ requirements.txt
├─ LICENSE
├─ .gitignore
├─ data/
│  ├─ raw/            # place original CSV(s) here (e.g., listings.csv)
│  └─ processed/      # cleaned data saved here
├─ notebooks/
│  └─ 01_eda_airbnb_london.ipynb
├─ reports/
│  └─ figures/        # exported plots
└─ src/
   ├─ prepare_data.py # cleaning/feature engineering to produce processed data
   └─ utils/
      └─ io.py        # small IO helpers
```

---

## 🗂️ Dataset

**How to get data:**
1) Download `listings.csv` (and optionally `calendar.csv`, `reviews.csv`) for **London** from the *Inside Airbnb* project site.  
2) Put the file(s) into `data/raw/` (keep the original filename, or update notebook arg).

---

## ❓ Business Questions 
1. **Pricing Landscape**: What’s the price distribution overall and by room type (Entire home/private room/shared)?  
2. **Location Effects**: How do prices vary by borough/neighbourhood? Where are the hottest clusters?  
3. **Supply & Quality Signals**: Does **number of reviews**, **ratings**, or **amenities** correlate with price?  
4. **Host Characteristics**: Do **superhost status** and **host tenure** (how long they’ve hosted) impact price?  
5. **Minimum Nights & Availability**: How do **minimum_nights** and **availability_365** relate to price?  
6. **Outliers & Data Quality**: Where are the outliers? What cleaning rules are justified?

---

## ▶️ Quickstart
```bash
# 1) Create and activate a fresh environment (optional, recommended)
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Put your data into data/raw/ e.g.
# data/raw/listings.csv

# 4) (Optional) Run cleaning script to create processed data
python src/prepare_data.py --input data/raw/listings.csv --output data/processed/listings_clean.csv

# 5) Open the notebook
jupyter notebook notebooks/01_eda_airbnb_london.ipynb
```

---

---

## 📝 Citation
If you publish, acknowledge the **Inside Airbnb** project and the specific London snapshot you used.

---

## 📄 License
This project is open‑sourced under the **MIT License**.
