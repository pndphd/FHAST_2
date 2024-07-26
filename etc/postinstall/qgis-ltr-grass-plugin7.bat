textreplace -std -t bin\qgis-ltr-grass7.bat

if "%OSGEO4W_DESKTOP%"=="" set OSGEO4W_DESKTOP=~$folder.common_desktop$

copy bin\qgis-ltr-bin.exe bin\qgis-ltr-bin-g7.exe
copy bin\qgis-ltr-bin.vars bin\qgis-ltr-bin-g7.vars
call "%OSGEO4W_ROOT%\bin\qgis-ltr-grass7.bat" --postinstall

if not %OSGEO4W_MENU_LINKS%==0 mkdir "%OSGEO4W_STARTMENU%"
if not %OSGEO4W_DESKTOP_LINKS%==0 mkdir "%OSGEO4W_DESKTOP%"

if not %OSGEO4W_MENU_LINKS%==0 nircmd shortcut "%OSGEO4W_ROOT%\bin\qgis-ltr-bin-g7.exe" "%OSGEO4W_STARTMENU%" "QGIS Desktop 3.16.11 with GRASS 7.8.5" "" "" "" "" "~$folder.mydocuments$"
if not %OSGEO4W_DESKTOP_LINKS%==0 nircmd shortcut "%OSGEO4W_ROOT%\bin\qgis-ltr-bin-g7.exe" "%OSGEO4W_DESKTOP%" "QGIS Desktop 3.16.11 with GRASS 7.8.5" "" "" "" "" "~$folder.mydocuments$"
