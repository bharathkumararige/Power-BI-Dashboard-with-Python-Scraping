# 📊 Power BI Dashboard with Python Web Scraping

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

> A complete end-to-end data pipeline — scraping real-time book data from the web using Python, cleaning it with Pandas, and visualizing it through an interactive Power BI dashboard.

---

## 📌 Project Overview

This project demonstrates a **full data analytics workflow** — from raw web data to business-ready visual insights. It scrapes book data from [books.toscrape.com](http://books.toscrape.com/), processes it with Python, and builds an interactive Power BI dashboard for analysis.

---

## 🚀 Pipeline Architecture

```
Web Source (books.toscrape.com)
     ↓
Python Web Scraping (requests + BeautifulSoup)
     ↓
Data Cleaning & Processing (Pandas)
     ↓
Export to CSV (booksc.csv)
     ↓
Import into Power BI
     ↓
Interactive Dashboard (books.pbix)
```

---

## ✨ Key Features

- 🕷️ **Web Scraping** — Automated data extraction using `requests` & `BeautifulSoup`
- 🧹 **Data Cleaning** — Structured and formatted using `Pandas`
- 📊 **Power BI Dashboard** — Interactive visualizations with filters & slicers
- 🔄 **End-to-End Pipeline** — From raw HTML to business insights
- 📁 **Reusable** — Easy to adapt for any website or dataset

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Web Scraping | Requests, BeautifulSoup4 |
| Data Processing | Pandas |
| Visualization | Power BI Desktop |
| Data Format | CSV |
| Environment | Jupyter Notebook |

---

## 📂 Project Structure

```
Power-BI-Dashboard-with-Python-Scraping/
│
├── scrap.ipynb          # Python web scraping notebook
├── booksc.csv           # Scraped & cleaned dataset
├── books.pbix           # Power BI dashboard file
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/bharathkumararige/Power-BI-Dashboard-with-Python-Scraping.git
cd Power-BI-Dashboard-with-Python-Scraping
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Scraper
```bash
jupyter notebook scrap.ipynb
```
Run all cells — this will scrape the data and save it as `booksc.csv`

### 4. Open Power BI Dashboard
- Open **Power BI Desktop**
- Open `books.pbix`
- Refresh data source to point to your local `booksc.csv`
- Explore the dashboard! 📊

---

## 📈 Dashboard Insights

The Power BI dashboard provides:
- 📚 **Book ratings distribution** across categories
- 💰 **Price analysis** by genre and rating
- 📦 **Stock availability** overview
- 🔍 **Interactive filters** to drill down by category/price/rating

---

## 💡 What I Learned

- End-to-end data pipeline from web to visualization
- Web scraping best practices with BeautifulSoup
- Data wrangling and cleaning with Pandas
- Building interactive dashboards in Power BI
- Connecting Python-generated data to Power BI

---

## 👨‍💻 Author

**Arige Bharath Kumar**
- 🎓 B.Tech CSE (Data Science) — Graduating July 2026
- 📧 [arigebharathkumar@gmail.com](mailto:arigebharathkumar@gmail.com)
- 🔗 [LinkedIn](https://linkedin.com/in/arigebharath)
- 🐙 [GitHub](https://github.com/bharathkumararige)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">⭐ <b>If you found this project helpful, please give it a star!</b> ⭐</p>

