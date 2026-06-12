@echo off
title AI Query Tool
cd /d "%~dp0"
echo Loading AI model...
python "%~dp0ai_query.py"
pause
