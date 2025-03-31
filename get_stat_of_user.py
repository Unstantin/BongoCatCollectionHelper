import json
import os
from dotenv import load_dotenv
import base64

load_dotenv()
#id = os.getenv('STEAM_ID')

def get_stat_of_user(steam_id):
    colors = {
        "B0B0B0": "common",
        "5ACC3D": "uncommon",
        "258ED4": "rare",
        "B939DB": "epic",
        "FFB000": "legendary"
    }

    user_count = {
        "B0B0B0": 0,
        "5ACC3D": 0,
        "258ED4": 0,
        "B939DB": 0,
        "FFB000": 0
    }
    user_items = None
    user_items_group_by_color = {
        "B0B0B0": [],
        "5ACC3D": [],
        "258ED4": [],
        "B939DB": [],
        "FFB000": []
    }
    set_user_items_classid = set()
    with open(f"items_{steam_id}.json", "r") as file:
        user_items = json.load(file)
        for item in user_items["descriptions"]:
            user_count[item['name_color']] += 1
            with open(f"icons/{item['name']}.jpg", "rb") as img:
                item["binary_image"] = base64.b64encode(img.read()).decode("utf-8")
            user_items_group_by_color[item['name_color']].append(item)
            set_user_items_classid.add(item['classid'])

    all_count = {
        "B0B0B0": 0,
        "5ACC3D": 0,
        "258ED4": 0,
        "B939DB": 0,
        "FFB000": 0
    }
    all_items = None
    other_items_group_by_color = {
        "B0B0B0": [],
        "5ACC3D": [],
        "258ED4": [],
        "B939DB": [],
        "FFB000": []
    }
    with open("items.json", "r") as file:
        all_items = json.load(file)
        for item in all_items:
            all_count[item['asset_description']['name_color']] += 1
            if item['asset_description']['classid'] not in set_user_items_classid:
                other_items_group_by_color[item['asset_description']['name_color']].append(item)

    stat = {"general": [], "collection": []}
    for value, name in colors.items():
        stat['general'].append({
            "name": name,
            "user_n": user_count[value],
            "all_n": all_count[value]
        })
        stat['collection'].append({
            "name": name,
            "user_items": user_items_group_by_color[value],
            "other_items": other_items_group_by_color[value]
        })

    with open("res.json", "w") as file:
        json.dump(stat, file, ensure_ascii=False, indent=4)

    return stat


#get_stat_of_user(id)
