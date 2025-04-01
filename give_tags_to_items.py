import json

count = 0
set_first_generation_id = set()
tag_to_class_id = dict()
with open("items_first_generation.json") as file:
    first_generation = json.load(file)
    print(len(first_generation))
    for item in first_generation:
        classid = item["asset_description"]["classid"]
        tag_to_class_id[classid] = "first_generation"
        set_first_generation_id.add(item["asset_description"]["classid"])

with open("items_april_event.json") as file:
    april_event = json.load(file)
    print(len(april_event))
    for item in april_event:
        classid = item["asset_description"]["classid"]
        if classid not in set_first_generation_id:
            tag_to_class_id[classid] = "april_event"

with open("tag_to_classid.json", "w") as file:
    json.dump(tag_to_class_id, file, ensure_ascii=False, indent=4)