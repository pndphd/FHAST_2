dllupdate -copy -reboot "%OSGEO4W_ROOT%\bin\opencl.dll"
if errorlevel 1 exit /b 1
if exist %WINDIR%\system32\opencl.dll del "%OSGEO4W_ROOT%\bin\opencl.dll"
