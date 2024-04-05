from ollama import Client

client = Client(host="http://macos-sonoma.local:11434")
response = client.chat(
    model="gemma:2b",
    messages=[
        {
            "role": "user",
            "content": "Quanto é a raiz quadrada de 49?",
        },
    ],
)
print(response["message"]["content"])
