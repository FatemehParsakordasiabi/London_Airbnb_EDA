# Airbnb London – Data Wrangling & EDA
End‑to‑end exploratory data analysis (EDA) and data cleaning project focused on **short‑term rental pricing in London**. This repo is designed to showcase **data wrangling, feature engineering, visualization, and storytelling**—exactly what hiring managers look for in a Data Scientist portfolio.

> **Goal:** Understand what drives listing prices in London and produce actionable insights with clean visuals and a polished narrative.

---

## 🔧 Project Highlights
- Real‑world messy data (listings with missing values, text fields, dates, categories).
- Reproducible workflow: `src/` scripts + a clean Jupyter notebook in `notebooks/`.
- Clear **questions → analyses → insights → visuals** pipeline.
- Ready to publish on GitHub: badges, structure, and a tidy README.

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
Use the **Inside Airbnb London** dataset (public) for a specific year/month. You typically need the file:
- `listings.csv` — main table with price, neighbourhood, host_since, room_type, reviews, etc.

**How to get data:**
1) Download `listings.csv` (and optionally `calendar.csv`, `reviews.csv`) for **London** from the *Inside Airbnb* project site.  
2) Put the file(s) into `data/raw/` (keep the original filename, or update notebook arg).

> **Tip:** Prefer the monthly snapshot closest to present day to keep the analysis fresh.

---

## ❓ Business Questions (use these as section headers)
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

## 🧹 Cleaning & Feature Engineering (implemented)
- **Price parsing**: strip currency symbols/commas → numeric `price_gbp`  
- **Date handling**: `host_since` → datetime, compute `host_tenure_days`  
- **Boolean flags**: `host_is_superhost`, `instant_bookable` → 0/1  
- **Text features (basic)**: count amenities in `amenities` column → `amenity_count`  
- **Winsorization** (optional): cap extreme price outliers for stable visuals

---

## 📊 Core Visuals (made easy in the notebook)
- Price distribution (histogram, log‑scale option)
- Price by room type (boxplot + summary stats)
- Price vs. reviews / rating / amenity_count (scatter + trendline)
- Price by neighbourhood (top 15; bar chart)
- Availability and minimum nights vs. price (binned plots)

> All charts are exported to `reports/figures/` so you can embed them in the README or slides.

---

## 🧠 What to Conclude (example angles)
- **Room type** is the biggest driver of price variance (entire homes >> private rooms).  
- **Central neighbourhoods** command price premiums; quantify uplift vs city median.  
- **Superhost & tenure** have modest but noticeable positive association with price.  
- **Amenity richness** matters up to a point; diminishing returns afterward.  
- **Outliers** suggest manual review or listing category issues.

Back your claims with **numbers** (medians, IQRs, effect sizes) and **plots**.

---

## ✅ Deliverables Checklist
- [ ] Clean EDA notebook with narrative & conclusions  
- [ ] Exported figures in `reports/figures/`  
- [ ] Reproducible cleaning script in `src/`  
- [ ] `README` with problem, methods, key findings, and next steps

---

## 🚀 Next Steps / Extensions
- Add **geospatial** analysis (borough shapefiles; choropleths).
- Enrich with **calendar** data to analyze seasonality & price elasticity.
- Build a **simple pricing model** (baseline regression with k‑fold CV).
- Wrap a **Streamlit** dashboard for interactive exploration.

---

## 📝 Citation
If you publish, acknowledge the **Inside Airbnb** project and the specific London snapshot you used.

---

## 📄 License
This project is open‑sourced under the **MIT License**.
