set ICON=%OSGEO4W_ROOT%\apps\grass\grass78\gui\icons\grass_osgeo.ico
set BATCH=%OSGEO4W_ROOT%\bin\grass78.bat
textreplace -std -t "%BATCH%"
textreplace -std -t "%OSGEO4W_ROOT%"\apps\grass\grass78\etc\fontcap

if not %OSGEO4W_MENU_LINKS%==0 xxmklink "%OSGEO4W_STARTMENU%\GRASS GIS 7.8.5.lnk" "%BATCH%"  "--gui" \ "Launch GRASS GIS 7.8.5" 1 "%ICON%" 
if not %OSGEO4W_DESKTOP_LINKS%==0 xxmklink "%OSGEO4W_DESKTOP%\GRASS GIS 7.8.5.lnk" "%BATCH%"  "--gui" \ "Launch GRASS GIS 7.8.5" 1 "%ICON%" 

rem run g.mkfontcap outside a GRASS session during
rem an OSGeo4W installation for updating paths to fonts

rem set gisbase
set GISBASE=%OSGEO4W_ROOT%\apps\grass\grass78

rem set path to freetype dll and its dependencies
set FREETYPEBASE=%OSGEO4W_ROOT%\bin;%OSGEO4W_ROOT%\apps\msys\bin;%GISBASE%\lib

rem set dependencies to path
set PATH=%FREETYPEBASE%;%PATH%

rem GISRC must be set
set GISRC=dummy

rem run g.mkfontcap outside a GRASS session
"%GISBASE%\bin\g.mkfontcap.exe" -o

del "%BATCH%.tmpl
