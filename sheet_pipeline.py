import gspread
from google.oauth2.service_account import Credentials
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

print("🔄 Initializing your data pipeline...")

# 1. LINK TO GOOGLE SHEETS VIA SECURE CREDENTIALS
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

try:
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open("Book_Scraper_Data").sheet1
    print("✅ Successfully connected to Google Sheets!")
except Exception as e:
    print(f"❌ Error connecting to Google Sheets: {e}")
    print("Please ensure 'credentials.json' is placed correctly in your sidebar.")
    exit()

# 2. RUN YOUR SCRAPER
print("🌐 Fetching fresh data from books.toscrape.com...")
url = "http://books.toscrape.com/catalogue/page-1.html"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    books_list = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("£", "").strip()
        availability = book.find("p", class_="instock availability").text.strip()
        
        books_list.append({
            "Book Title": title,
            "Price (GBP)": float(price),
            "Stock Status": availability
        })

    # Clean and structure using Pandas
    df = pd.DataFrame(books_list)
    df["Pipeline Run Time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"✅ Scraped {len(df)} records into a Pandas DataFrame.")

    # 3. PUSH FRESH DATA TO GOOGLE SHEETS
    print("🧹 Clearing old data and updating your Google Sheet...")
    sheet.clear()  
    
    upload_data = [df.columns.tolist()] + df.values.tolist()
    sheet.update("A1", upload_data)
    
    print("\n🚀 PIPELINE SUCCESSFUL: Check your live 'Book_Scraper_Data' Google Sheet!")

except Exception as e:
    print(f"❌ Pipeline failed: {e}")