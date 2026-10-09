import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

def search_target(query):
    search_query = query.replace(" ", "+")
    API_KEY = os.getenv("Key")
    url = f"https://data.unwrangle.com/api/getter/?platform=target_search&search={search_query}&api_key={API_KEY}"

    response = requests.get(url)
    response.raise_for_status()
    target_data = response.json()

    with open('Target_output.json','a',encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)

    print("wrote the data to json")
    
search_target('Laptop')
