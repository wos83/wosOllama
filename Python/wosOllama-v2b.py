import asyncio
from ollama import AsyncClient


async def generate():
    client = AsyncClient(host="http://macos-sonoma.local:11434")
    prompt = "Quanto é a raiz quadrada de 49?"
    response = await client.generate(
        model="gemma:2b",
        prompt=prompt,
    )
    print(response["response"])


asyncio.run(generate())
