@echo off
cd /d "%~dp0"

:: Auto-create .env from .env.example if missing
if not exist ".env" (
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo.
        echo  [JARVIS] .env not found — created from .env.example
        echo  [JARVIS] Open .env and add your GROQ_API_KEY before continuing.
        echo.
        notepad .env
        echo  Press any key after saving your API keys...
        pause >nul
    ) else (
        echo  [JARVIS] WARNING: No .env file found. JARVIS may not work correctly.
        pause >nul
    )
)

:: Start backend in new window
start "JARVIS Backend" python server.py

:: Start frontend in current window
cd frontend
npm run dev
