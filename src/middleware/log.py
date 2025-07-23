import httpx

async def log(params):
    testapiserver = "http://20.244.56.144/evaluation-service/auth"
    async with httpx.AsyncClient() as client:
        response = await client.post(testapiserver, json=params)
        response.raise_for_status()
        return response.json()
    