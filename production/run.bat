@echo off
set /p com=Entrez port COM : 

echo.
echo [1/3] Fermeture des processus qui pourraient bloquer le port...
taskkill /IM arduino.exe /F >nul 2>&1
taskkill /IM putty.exe /F >nul 2>&1

echo.
echo [2/3] Flash de l'ESP32...
python -m esptool --chip esp32 --port %com% --baud 460800 write_flash -z 0x0 YOUR_PATH\Python-Monitor\production\firmware.bin 

echo Débranchez et rebranchez l'ESP
pause

echo.
echo Attente que le port %com% soit de nouveau prêt...
:waitForPort
mode %com% >nul 2>&1
if errorlevel 1 (
    timeout /t 1 >nul
    goto waitForPort
)

type nul > firmware-clt\values.h

echo.
echo [3/3] Enregistrement de l'ESP...
python register_esp.py -p %com%

arduino-cli compile --fqbn esp32:esp32:esp32 YOUR_PATH\Python-Monitor\production\firmware-clt\firmware-clt.ino
arduino-cli upload -p %com% --fqbn esp32:esp32:esp32 YOUR_PATH\Python-Monitor\production\firmware-clt\firmware-clt.ino

del /f /q firmware-clt\values.h


pause
