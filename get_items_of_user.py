import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
#steam_id = os.getenv('STEAM_ID')


def get_items_of_user(steam_id):
    def get_steam_inventory(steam_id):
        url = f"https://steamcommunity.com/inventory/{steam_id}/3419430/2"
        params = {
            'count': 5000
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            return None


    inventory = get_steam_inventory(steam_id)
    with open(f"items_{steam_id}.json", "w") as file:
        json.dump(inventory, file, ensure_ascii=False, indent=4)

