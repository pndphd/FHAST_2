for %%f in ("%TEMP%") do call set TEMPDRIVE=%%~df
cd %TEMP%

"%OSGEO4W_ROOT%\bin\vcredist-2010-x64.exe" /q /norestart
if errorlevel 3010 echo>"%OSGEO4W_ROOT%\etc\reboot"
del "%OSGEO4W_ROOT%\bin\vcredist-2010-x64.exe"
