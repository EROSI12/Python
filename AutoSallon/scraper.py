import requests
from bs4 import BeautifulSoup

def scrape_car_brands():
    try:
        url = "https://quotes.toscrape.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        authors = soup.find_all("small", class_="author")
        brands = [a.text for a in authors[:5]]
        return brands
    except Exception as e:
        print("Scraper error:", e)
        return []