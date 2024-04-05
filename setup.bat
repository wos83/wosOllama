@echo off
chcp 65001

python --version
python -m pip install --upgrade pip

python -m pip install asyncio
python -m pip install mistune
python -m pip install translang
python -m pip install ollama
