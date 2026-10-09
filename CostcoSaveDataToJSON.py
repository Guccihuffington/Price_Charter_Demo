import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

def search_costco(query):
    search_query = query.replace(" ", "+")
    API_KEY = os.getenv("Key")
    url = f"https://data.unwrangle.com/api/getter/?platform=costco_search&search={search_query}&api_key={API_KEY}"

    response = requests.get(url)
    response.raise_for_status()
    costco_data = response.json()

    with open('Costco_Output.json','a',encoding='utf-8') as f:
        json.dump(costco_data, f, ensure_ascii=False, indent=4)

    print("wrote the data to json")
    
search_costco('Laptop')
