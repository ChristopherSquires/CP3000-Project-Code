@echo off
:: ============================================================
:: setup_windows.bat – One-click setup for CP3000 on Windows
::
:: What this script does:
::   1. Enables Windows Long Path support (requires admin rights).
::   2. Creates a virtual environment at C:\cp3000\.venv so the
::      path stays short enough for TensorFlow's deep header tree.
::   3. Installs all project dependencies.
::
:: Run from an elevated (Administrator) command prompt:
::   setup_windows.bat
:: ============================================================

:: ---- 1. Enable Long Path support ----------------------------
echo Enabling Windows Long Path support...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" ^
    /v LongPathsEnabled /t REG_DWORD /d 1 /f >nul 2>&1
set LONGPATH_OK=%ERRORLEVEL%
if %LONGPATH_OK% NEQ 0 (
    echo.
    echo ERROR: Could not enable Long Paths - administrator rights are required.
    echo Please re-run this script from an elevated ^(Administrator^) command prompt.
    echo.
    echo Alternatively, enable Long Path support manually before running setup:
    echo   1. Open Registry Editor ^(regedit.exe^)
    echo   2. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
    echo   3. Set LongPathsEnabled to 1
    echo   - OR -
    echo   Open an elevated PowerShell and run:
    echo     New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" ^
    echo       -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force
    echo.
    echo Then REBOOT and run this script again.
    exit /b 1
)
echo Long Path support enabled. A reboot is required for it to take effect.
echo This script will continue with a short venv path so pip can succeed without a reboot.
echo After setup completes, reboot before doing further work that relies on long paths.

:: ---- 2. Create venv at a short path -------------------------
set VENV_DIR=C:\cp3000\.venv
echo.
echo Creating virtual environment at %VENV_DIR% ...
if not exist C:\cp3000 mkdir C:\cp3000
python -m venv "%VENV_DIR%"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create virtual environment. Is Python installed?
    exit /b 1
)

:: ---- 3. Install dependencies --------------------------------
echo.
echo Installing dependencies from requirements.txt ...
"%VENV_DIR%\Scripts\pip" install --upgrade pip
"%VENV_DIR%\Scripts\pip" install -r "%~dp0requirements.txt"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: pip install failed.
    echo The virtual environment is already at a short path, so if you see a
    echo long-path error here it is likely caused by pip's own temporary files.
    echo Reboot your machine to fully activate the Long Path registry setting,
    echo then run this script again.
    exit /b 1
)

echo.
echo ============================================================
echo Setup complete!
echo Activate the environment with:
echo   %VENV_DIR%\Scripts\activate
echo Then run the app with:
echo   streamlit run app.py
echo ============================================================
