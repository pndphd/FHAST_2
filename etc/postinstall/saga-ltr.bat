if "%OSGEO4W_DESKTOP%"=="" set OSGEO4W_DESKTOP=%ALLUSERSPROFILE%\Desktop

if not %OSGEO4W_DESKTOP_LINKS%==0 mkdir "%OSGEO4W_DESKTOP%"
if not %OSGEO4W_DESKTOP_LINKS%==0 nircmd shortcut "%OSGEO4W_ROOT%\bin\nircmd.exe" "%OSGEO4W_DESKTOP%" "SAGA GIS (2.3.2)" "exec hide ~q%OSGEO4W_ROOT%\bin\saga-ltr_gui.bat~q" "%OSGEO4W_ROOT%\apps\saga-ltr\saga_gui.exe"

if not %OSGEO4W_MENU_LINKS%==0 mkdir "%OSGEO4W_STARTMENU%"
if not %OSGEO4W_MENU_LINKS%==0 nircmd shortcut "%OSGEO4W_ROOT%\bin\nircmd.exe" "%OSGEO4W_STARTMENU%" "SAGA GIS (2.3.2)" "exec hide ~q%OSGEO4W_ROOT%\bin\saga-ltr_gui.bat~q" "%OSGEO4W_ROOT%\apps\saga-ltr\saga_gui.exe"
