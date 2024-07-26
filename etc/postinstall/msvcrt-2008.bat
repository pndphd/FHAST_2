for %%f in ("%TEMP%") do call set TEMPDRIVE=%%~df
cd %TEMP%

"%OSGEO4W_ROOT%\bin\vcredist-2008-sp1-x64.exe" /q
if errorlevel 3010 echo>"%OSGEO4W_ROOT%\etc\reboot"
del "%OSGEO4W_ROOT%\bin\vcredist-2008-sp1-x64.exe"
