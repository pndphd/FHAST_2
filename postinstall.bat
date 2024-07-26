@echo off
if exist postinstall.log del postinstall.log
set OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT:\=/%>>postinstall.log 2>&1
if "%OSGEO4W_ROOT_MSYS:~1,1%"==":" set OSGEO4W_ROOT_MSYS=/%OSGEO4W_ROOT_MSYS:~0,1%/%OSGEO4W_ROOT_MSYS:~3%>>postinstall.log 2>&1
del preremove-conf.bat>>postinstall.log 2>&1
echo set OSGEO4W_ROOT=%OSGEO4W_ROOT%>>preremove-conf.bat
echo set OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT_MSYS%>>preremove-conf.bat
echo set OSGEO4W_STARTMENU=%OSGEO4W_STARTMENU%>>preremove-conf.bat
echo set OSGEO4W_DESKTOP=%OSGEO4W_DESKTOP%>>preremove-conf.bat
echo OSGEO4W_ROOT=%OSGEO4W_ROOT%>>postinstall.log 2>&1
echo OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT_MSYS%>>postinstall.log 2>&1
echo OSGEO4W_STARTMENU=%OSGEO4W_STARTMENU%>>postinstall.log 2>&1
echo OSGEO4W_DESKTOP=%OSGEO4W_DESKTOP%>>postinstall.log 2>&1
PATH %OSGEO4W_ROOT%\bin;%PATH%>>postinstall.log 2>&1
cd /d %OSGEO4W_ROOT%>>postinstall.log 2>&1
echo Running postinstall grass.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\grass.bat>>postinstall.log 2>&1
ren etc\postinstall\grass.bat grass.bat.done>>postinstall.log 2>&1
echo Running postinstall liblas.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\liblas.bat>>postinstall.log 2>&1
ren etc\postinstall\liblas.bat liblas.bat.done>>postinstall.log 2>&1
echo Running postinstall msvcrt-2008.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt-2008.bat>>postinstall.log 2>&1
ren etc\postinstall\msvcrt-2008.bat msvcrt-2008.bat.done>>postinstall.log 2>&1
echo Running postinstall msvcrt-2010.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt-2010.bat>>postinstall.log 2>&1
ren etc\postinstall\msvcrt-2010.bat msvcrt-2010.bat.done>>postinstall.log 2>&1
echo Running postinstall msvcrt-2013.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt-2013.bat>>postinstall.log 2>&1
ren etc\postinstall\msvcrt-2013.bat msvcrt-2013.bat.done>>postinstall.log 2>&1
echo Running postinstall netcdf.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\netcdf.bat>>postinstall.log 2>&1
ren etc\postinstall\netcdf.bat netcdf.bat.done>>postinstall.log 2>&1
echo Running postinstall opencl.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\opencl.bat>>postinstall.log 2>&1
ren etc\postinstall\opencl.bat opencl.bat.done>>postinstall.log 2>&1
echo Running postinstall openssl.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\openssl.bat>>postinstall.log 2>&1
ren etc\postinstall\openssl.bat openssl.bat.done>>postinstall.log 2>&1
echo Running postinstall openssl10.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\openssl10.bat>>postinstall.log 2>&1
ren etc\postinstall\openssl10.bat openssl10.bat.done>>postinstall.log 2>&1
echo Running postinstall pyqt5.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\pyqt5.bat>>postinstall.log 2>&1
ren etc\postinstall\pyqt5.bat pyqt5.bat.done>>postinstall.log 2>&1
echo Running postinstall python3-pip.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\python3-pip.bat>>postinstall.log 2>&1
ren etc\postinstall\python3-pip.bat python3-pip.bat.done>>postinstall.log 2>&1
echo Running postinstall python3-setuptools.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\python3-setuptools.bat>>postinstall.log 2>&1
ren etc\postinstall\python3-setuptools.bat python3-setuptools.bat.done>>postinstall.log 2>&1
echo Running postinstall qgis-ltr-common.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\qgis-ltr-common.bat>>postinstall.log 2>&1
ren etc\postinstall\qgis-ltr-common.bat qgis-ltr-common.bat.done>>postinstall.log 2>&1
echo Running postinstall qgis-ltr-grass-plugin-common.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\qgis-ltr-grass-plugin-common.bat>>postinstall.log 2>&1
ren etc\postinstall\qgis-ltr-grass-plugin-common.bat qgis-ltr-grass-plugin-common.bat.done>>postinstall.log 2>&1
echo Running postinstall qgis-ltr-grass-plugin7.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\qgis-ltr-grass-plugin7.bat>>postinstall.log 2>&1
ren etc\postinstall\qgis-ltr-grass-plugin7.bat qgis-ltr-grass-plugin7.bat.done>>postinstall.log 2>&1
echo Running postinstall qgis-ltr.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\qgis-ltr.bat>>postinstall.log 2>&1
ren etc\postinstall\qgis-ltr.bat qgis-ltr.bat.done>>postinstall.log 2>&1
echo Running postinstall qt5-libs.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\qt5-libs.bat>>postinstall.log 2>&1
ren etc\postinstall\qt5-libs.bat qt5-libs.bat.done>>postinstall.log 2>&1
echo Running postinstall saga-ltr.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\saga-ltr.bat>>postinstall.log 2>&1
ren etc\postinstall\saga-ltr.bat saga-ltr.bat.done>>postinstall.log 2>&1
echo Running postinstall setup.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\setup.bat>>postinstall.log 2>&1
ren etc\postinstall\setup.bat setup.bat.done>>postinstall.log 2>&1
echo Running postinstall shell.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\shell.bat>>postinstall.log 2>&1
ren etc\postinstall\shell.bat shell.bat.done>>postinstall.log 2>&1
echo Running postinstall sip-qt5.bat...>>postinstall.log 2>&1
%COMSPEC% /c etc\postinstall\sip-qt5.bat>>postinstall.log 2>&1
ren etc\postinstall\sip-qt5.bat sip-qt5.bat.done>>postinstall.log 2>&1
ren postinstall.bat postinstall.bat.done>>postinstall.log 2>&1
