# 📊 Automated Google Sheets powerBI Dashboard with Python Web Scraping

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
</p>

> A complete end-to-end data pipeline — scraping real-time book data from the web using Python, cleaning it with Pandas, and automatically streaming it to a cloud-based Google Sheets dashboard.

---

## 📌 Project Overview

This project demonstrates a **modern cloud data engineering workflow**. Instead of managing brittle local files, this pipeline automates data extraction from [books.toscrape.com](http://books.toscrape.com/), cleans it on the fly, and uses secure Google Cloud Service Account APIs to stream data directly into a cloud-hosted Google Sheet dashboard for instant visualization.

---

## 🚀 Pipeline Architecture
Web Source (books.toscrape.com)
↓
Python Web Scraping (requests + BeautifulSoup)
↓
Data Cleaning & Processing (Pandas)
↓
Cloud Pipeline Automation (gspread + Google Service Account)
↓
Live Cloud Data Layer (Google Sheets - 'Book_Scraper_Data')
↓
Automated Dashboard & Visualizations (power BI / Google Sheets )
---

## ✨ Key Features

- 🕷️ **Automated Web Scraping** — Real-time data extraction using `requests` & `BeautifulSoup4`.
- 🧹 **In-Memory Transformation** — Seamless data cleaning and structure formatting using `Pandas`.
- ☁️ **Live Cloud Streaming** — Server-to-server cloud connection using `gspread` and Google Cloud Service Accounts.
- 🔒 **Security First** — Explicit environment protection using `.gitignore` to keep API security credentials off public repositories.
- 🔄 **Real-Time Visualization** — Cloud-hosted interactive dashboard that updates instantly when the pipeline runs.

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.x |
| **Web Scraping** | Requests, BeautifulSoup4 |
| **Data Processing** | Pandas |
| **Cloud Automation** | Gspread, Google Cloud Console (Drive & Sheets APIs) |
| **Visualization** | Google Sheets  / power BI|
| **Environment** | VS Code / Jupyter Notebook |

---

## 📂 Project Structure
Power-BI-Dashboard-with-Python-Scraping/
│
├── sheet_pipeline.py    # Main automated automation production script
├── scrap.ipynb          # Python web scraping scratchpad/notebook
├── requirements.txt     # Production dependencies and libraries
├── .gitignore           # Explicitly hides credentials.json from git staging
└── README.md
Note: The project requires a local `credentials.json` file in the root directory to authorize cloud updates, which is safely hidden via `.gitignore`.

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone [https://github.com/bharathkumararige/Power-BI-Dashboard-with-Python-Scraping.git](https://github.com/bharathkumararige/Power-BI-Dashboard-with-Python-Scraping.git)
cd Power-BI-Dashboard-with-Python-Scraping
2. Install Dependencies
pip install -r requirements.txt
3. Setup Credentials
Generate a Service Account key (credentials.json) via your Google Cloud Console.
Enable both the Google Sheets API and Google Drive API in your cloud console project.
Place your credentials.json directly into this project's folder.
Share your Google Sheet (Book_Scraper_Data) with the client email address found inside your credentials.json.
4. Run the Pipeline
python sheet_pipeline.py
The terminal will scrape 20 live records, connect to the cloud, refresh the data layout, and update your cloud sheet instantly!
📈 Dashboard Insights
The live Google Sheets dashboard tracks:
📚 Book ratings distribution across web categories.
💰 Price analysis metrics by genre and stock levels.
📦 Stock availability status maps.
📊 Dynamic Charts that redraw automatically upon script completion without needing a manual refresh button.
💡 What I Learned
Designing decoupled cloud data pipelines without relying on rigid local storage files.
Managing secure authentication profiles using service accounts and Google Cloud Manager.
Securing production files and preventing API token exposure on GitHub using .gitignore.
Integrating automated Python scraping routines directly into cloud visualization software.


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

