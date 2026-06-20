@echo off

if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Installing requirements...
.venv\Scripts\python.exe -m pip install -r requirements.txt

echo Starting bot...
.venv\Scripts\python.exe bot.py

pause