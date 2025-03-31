import time
import requests
import json

appid = 3419430
items = []

def wait_for_good_code(response):
    while response.status_code // 100 != 2:
        print(response.status_code)
        response = requests.get(url)
        time.sleep(60)
    return response


url = f"https://steamcommunity.com/market/search/render/?query=&start=1&count=100&search_descriptions=0&sort_column=price&sort_dir=asc&appid={appid}&norender=1"
response = wait_for_good_code(requests.get(url))
data = response.json()
total_count = data["total_count"]
pages_n = total_count // 10 + 1
print("pages_n:", pages_n)
for i in range(pages_n):
    url = f"https://steamcommunity.com/market/search/render/?query=&start={i*100}&count=100&search_descriptions=0&sort_column=price&sort_dir=asc&appid={appid}&norender=1"
    response = wait_for_good_code(requests.get(url))
    data = response.json()
    items += data["results"]

with open("items.json", "w") as file:
    json.dump(items, file, ensure_ascii=False, indent=4)
