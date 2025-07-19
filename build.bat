@echo off
echo Building Voice Recorder Application...
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Building executable...
pyinstaller --onefile --console --name "VoiceRecorder" record_dataset.py

echo.
echo Build completed! Check the 'dist' folder for the executable.
pause
