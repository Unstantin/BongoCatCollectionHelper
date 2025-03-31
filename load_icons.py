import json
import os
import aiohttp
import asyncio


async def download_icon_async(session, icon_hash, item_name, output_dir="icons"):
    if not icon_hash:
        return None

    url = f"https://community.akamai.steamstatic.com/economy/image/{icon_hash}/"
    safe_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in item_name)
    filename = os.path.join(output_dir, f"{safe_name}.jpg")

    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    f.write(await response.read())
                print(f"Скачано: {filename}")
    except Exception as e:
        print(f"Ошибка: {item_name} - {e}")


async def download_all_icons(items):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for item in items:
            icon_hash = item["asset_description"]["icon_url"]
            item_name = item["name"]
            tasks.append(download_icon_async(session, icon_hash, item_name))
        await asyncio.gather(*tasks)


with open('items.json', 'r', encoding='utf-8') as file:
    items = json.load(file)
    asyncio.run(download_all_icons(items))