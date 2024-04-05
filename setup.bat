@echo off
chcp 65001

python --version
python -m pip install --upgrade pip

pip install asyncio
pip install mistune
pip install translang
