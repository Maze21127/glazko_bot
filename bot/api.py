import aiohttp


async def get_message(message_type: str):
    async with aiohttp.ClientSession() as session:
        url = f"http://127.0.0.1:6571/api/messages/{message_type}"
        async with session.get(url) as resp:
            response = await resp.json()
            return response['text']
