import asyncio
import aiohttp
import time

url = "https://zerodayreloaded.online/test/count.php"

async def send_request(session, random_id):
    payload = {
        "update_id": 936201006,
        "message": {
            "message_id": 1642380,
            "from": {
                "id": random_id,
                "is_bot": False,
                "first_name": "Name",
                "username": "Username",
                "language_code": "ru"
            },
            "chat": {
                "id": random_id,
                "first_name": "Name",
                "username": "Username",
                "type": "private"
            },
            "date": 1710849421,
            "text": "Test"
        }
    }

    async with session.post(url, json=payload) as response:
        if response.status != 200:
            print(f"Request failed with status: {response.status}")

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        with open("./ids.txt", "r") as file:
            ids = file.readlines()
        for random_id in ids:
            tasks.append(send_request(session, random_id.strip()))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Finished in {time.time() - start_time} seconds")
