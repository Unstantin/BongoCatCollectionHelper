import json

sorted_items = None
with open('items_first_generation.json', 'r', encoding='utf-8') as file:
    items = json.load(file)
    sorted_items = sorted(items, key=lambda x: x['name'])
    for item in sorted_items:
        print(item["name"])
        item['type'] = int(input())

with open('items_first_generation.json', 'w', encoding='utf-8') as file:
    json.dump(items, file, ensure_ascii=False, indent=4)