# 🇰🇪 Kenya Economic Pulse Dashboard

An interactive dashboard tracking Kenya's key macroeconomic and financial indicators over time — built to make national economic data accessible, visual, and easy to explore.

**🔗 Live App:** [kenya-economic-pulse-dashboard-72wqzgudhanpdxfjbtcjpr.streamlit.app](https://kenya-economic-pulse-dashboard-72wqzgudhanpdxfjbtcjpr.streamlit.app/)

---

## Overview

This project pulls together annual macroeconomic data from the **World Bank** and monthly financial data from the **Central Bank of Kenya (CBK)** into a single, interactive Streamlit dashboard. It's designed to answer a simple question: *what does Kenya's economy actually look like right now, and how has it moved over time?*

## Features

- **Macro Trends (Annual)** — GDP growth, inflation, and unemployment from World Bank data, with an interactive multi-select to toggle indicators on and off
- **Private Sector Credit Growth (Monthly)** — CBK credit growth trends over a 135-month period, with a cleaned-up time axis for readability
- **Mobile Money Trends (Monthly)** — M-Pesa transaction values (KSh billions) and registered account growth (millions), plotted side by side since they sit on very different scales
- **Latest Snapshot** — a KPI row surfacing the most recent GDP growth, inflation, credit growth, and M-Pesa transaction figures at a glance

## Data Sources

| Dataset | Source | Frequency |
|---|---|---|
| GDP growth, inflation, unemployment | World Bank API | Annual |
| Private sector credit growth | Central Bank of Kenya (CBK) | Monthly |
| Mobile money transaction value & accounts | Central Bank of Kenya (CBK) | Monthly |

Raw data was pulled and cleaned in a Jupyter notebook (`notebooks/data_pipeline.ipynb`), then saved as processed CSVs used directly by the app — this keeps the deployed dashboard fast and independent of live API calls.

## Tech Stack

- **Python**
- **Streamlit** — app framework
- **Pandas** — data wrangling
- **Plotly Express** — interactive charts

## Project Structure

```
kenya-economic-pulse-dashboard/
├── app.py                          # Streamlit app
├── requirements.txt
├── data/
│   └── processed/
│       ├── worldbank_indicators.csv
│       ├── cbk_credit_growth.csv
│       └── cbk_mobile_money.csv
└── notebooks/
    └── data_pipeline.ipynb         # Data extraction & cleaning
```

## Running Locally

```bash
git clone https://github.com/Tee-ai63/kenya-economic-pulse-dashboard.git
cd kenya-economic-pulse-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Author

**Tess Kamau**
[LinkedIn](https://linkedin.com/in/tesskamau) · [GitHub](https://github.com/Tee-ai63)
