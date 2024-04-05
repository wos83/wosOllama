import asyncio
import aiohttp
import sqlite3
import datetime
import os


async def make_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            response_data = await response.json()
            return response_data


async def main():
    
    start_time = datetime.datetime.now()

    directory = os.path.join(os.getcwd(), "Python")
    file_db = os.path.join(directory, "wosOllama-v1a.db")

    if not os.path.exists(directory):
        os.mkdir(directory)

    # Conexão com o banco de dados SQLite
    connection = sqlite3.connect(file_db)
    cursor = connection.cursor()

    create_table = """        
        CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        ,data TEXT
        ,response TEXT
        ,execution_time DATETIME
        )
        """

    # Cria o banco de dados
    cursor.execute(create_table)

    server = "macos-sonoma.local"
    port = 11434

    model = "gemma:2b"
    prompt = """Atue como um Desenvolvedor Sênior de Aplicações. Como usar o Delphi (da empresa Embarcadero) e o Python na versão 3 no mesmo Projeto?"""

    # Dados da requisição
    url = f"http://{server}:{port}/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "raw": True,
        "options": {
            "temperature": 0,
            "numa": False,
            "num_ctx": 1024,
            "num_batch": 2,
            "num_gqa": 1,
            "num_gpu": 1,
            "num_thread": 4,
            "main_gpu": 0,
            "low_vram": True,
        },
    }

    response_data = await make_request(url, data)

    end_time = datetime.datetime.now()
    execution_time = end_time - start_time

    # Conexão com o banco de dados SQLite
    connection = sqlite3.connect(file_db)
    cursor = connection.cursor()

    insert_table = """
        INSERT INTO requests (data, response, execution_time)
        VALUES (?, ?, ?)
        """

    # Inserindo dados no banco de dados
    cursor.execute(
        insert_table,
        (
            str(data),
            str(response_data),
            str(execution_time),
        ),
    )

    connection.commit()
    connection.close()

    print("")
    print(response_data["response"])
    print("")
    print(execution_time)
    print("")


if __name__ == "__main__":
    asyncio.run(main())
