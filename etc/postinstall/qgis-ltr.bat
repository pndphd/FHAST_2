textreplace -std -t bin\qgis-ltr.bat
textreplace -std -t bin\qgis-ltr-designer.bat
textreplace -std -t bin\python-qgis-ltr.bat
textreplace -std -t bin\qgis_process-qgis-ltr.bat

REM get short path without blanks
for %%i in ("%OSGEO4W_ROOT%") do set O4W_ROOT=%%~fsi
if "%OSGEO4W_DESKTOP%"=="" set OSGEO4W_DESKTOP=~$folder.common_desktop$

call "%OSGEO4W_ROOT%\bin\qgis-ltr.bat" --postinstall

if not %OSGEO4W_MENU_LINKS%==0 mkdir "%OSGEO4W_STARTMENU%"
if not %OSGEO4W_DESKTOP_LINKS%==0 mkdir "%OSGEO4W_DESKTOP%"

if not %OSGEO4W_MENU_LINKS%==0 nircmd shortcut "%O4W_ROOT%\bin\qgis-ltr-bin.exe" "%OSGEO4W_STARTMENU%" "QGIS Desktop 3.16.11" "" "" "" "" "~$folder.mydocuments$"
if not %OSGEO4W_DESKTOP_LINKS%==0 nircmd shortcut "%O4W_ROOT%\bin\qgis-ltr-bin.exe" "%OSGEO4W_DESKTOP%" "QGIS Desktop 3.16.11" "" "" "" "" "~$folder.mydocuments$"

if not %OSGEO4W_MENU_LINKS%==0 nircmd shortcut "%O4W_ROOT%\bin\nircmd.exe" "%OSGEO4W_STARTMENU%" "Qt Designer with QGIS 3.16.11 custom widgets" "exec hide """%OSGEO4W_ROOT%\bin\qgis-ltr-designer.bat"" "%O4W_ROOT%\apps\qgis-ltr\icons\QGIS.ico" "" "" "~$folder.mydocuments$"
if not %OSGEO4W_DESKTOP_LINKS%==0 nircmd shortcut "%O4W_ROOT%\bin\nircmd.exe" "%OSGEO4W_DESKTOP%" "Qt Designer with QGIS 3.16.11 custom widgets" "exec hide %O4W_ROOT%\bin\qgis-ltr-designer.bat" "%O4W_ROOT%\apps\qgis-ltr\icons\QGIS.ico" "" "" "~$folder.mydocuments$"

set OSGEO4W_ROOT=%OSGEO4W_ROOT:\=\\%
textreplace -std -t "%O4W_ROOT%\apps\qgis-ltr\bin\qgis.reg"
nircmd elevate "%WINDIR%\regedit" /s "%O4W_ROOT%\apps\qgis-ltr\bin\qgis.reg"
del /s /q "%OSGEO4W_ROOT%\apps\qgis-ltr\python\*.pyc"
exit /b 0
