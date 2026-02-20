import requests

def get_usd_to_eur():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data["rates"]["EUR"]
    except Exception as e:
        print("API error:", e)
        return None


def get_exchange_rate():
    return None