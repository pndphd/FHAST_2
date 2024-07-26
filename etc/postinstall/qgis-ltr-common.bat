call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
call qt5_env.bat
path %PATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\bin
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis-ltr
"%OSGEO4W_ROOT%\apps\qgis-ltr\crssync"
