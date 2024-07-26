@echo off
call "%~dp0\preremove-conf.bat">>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo OSGEO4W_ROOT=%OSGEO4W_ROOT%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo OSGEO4W_STARTMENU=%OSGEO4W_STARTMENU%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo OSGEO4W_DESKTOP=%OSGEO4W_DESKTOP%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
set OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT:\=/%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
if "%OSGEO4W_ROOT_MSYS:~1,1%"==":" set OSGEO4W_ROOT_MSYS=/%OSGEO4W_ROOT_MSYS:~0,1%/%OSGEO4W_ROOT_MSYS:~3%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT_MSYS%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
PATH %OSGEO4W_ROOT%\bin;%PATH%>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
cd /d "%OSGEO4W_ROOT%">>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove grass.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\grass.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\grass.bat grass.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove netcdf.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\netcdf.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\netcdf.bat netcdf.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove opencl.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\opencl.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\opencl.bat opencl.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove pyqt5.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\pyqt5.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\pyqt5.bat pyqt5.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-certifi.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-certifi.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-certifi.bat python3-certifi.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-chardet.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-chardet.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-chardet.bat python3-chardet.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-core.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-core.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-core.bat python3-core.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-coverage.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-coverage.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-coverage.bat python3-coverage.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-cycler.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-cycler.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-cycler.bat python3-cycler.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-decorator.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-decorator.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-decorator.bat python3-decorator.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-exifread.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-exifread.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-exifread.bat python3-exifread.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-future.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-future.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-future.bat python3-future.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-httplib2.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-httplib2.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-httplib2.bat python3-httplib2.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-idna.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-idna.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-idna.bat python3-idna.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-jinja2.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-jinja2.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-jinja2.bat python3-jinja2.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-markupsafe.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-markupsafe.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-markupsafe.bat python3-markupsafe.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-mock.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-mock.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-mock.bat python3-mock.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-networkx.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-networkx.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-networkx.bat python3-networkx.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-nose2.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-nose2.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-nose2.bat python3-nose2.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-numpy.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-numpy.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-numpy.bat python3-numpy.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-owslib.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-owslib.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-owslib.bat python3-owslib.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pandas.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pandas.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pandas.bat python3-pandas.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pbr.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pbr.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pbr.bat python3-pbr.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pillow.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pillow.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pillow.bat python3-pillow.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pip.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pip.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pip.bat python3-pip.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-plotly.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-plotly.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-plotly.bat python3-plotly.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-ply.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-ply.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-ply.bat python3-ply.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pyopengl.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pyopengl.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pyopengl.bat python3-pyopengl.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pyproj.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pyproj.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pyproj.bat python3-pyproj.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-python-dateutil.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-python-dateutil.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-python-dateutil.bat python3-python-dateutil.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pytz.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pytz.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pytz.bat python3-pytz.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pywin32.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pywin32.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pywin32.bat python3-pywin32.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-pyyaml.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pyyaml.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-pyyaml.bat python3-pyyaml.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-requests.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-requests.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-requests.bat python3-requests.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-retrying.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-retrying.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-retrying.bat python3-retrying.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-scipy.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-scipy.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-scipy.bat python3-scipy.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-setuptools.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-setuptools.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-setuptools.bat python3-setuptools.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-shapely.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-shapely.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-shapely.bat python3-shapely.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-simplejson.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-simplejson.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-simplejson.bat python3-simplejson.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-six.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-six.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-six.bat python3-six.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-urllib3.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-urllib3.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-urllib3.bat python3-urllib3.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-xlrd.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-xlrd.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-xlrd.bat python3-xlrd.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove python3-xlwt.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-xlwt.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\python3-xlwt.bat python3-xlwt.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove qgis-ltr-grass-plugin-common.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\qgis-ltr-grass-plugin-common.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\qgis-ltr-grass-plugin-common.bat qgis-ltr-grass-plugin-common.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove qgis-ltr-grass-plugin7.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\qgis-ltr-grass-plugin7.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\qgis-ltr-grass-plugin7.bat qgis-ltr-grass-plugin7.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove qgis-ltr.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\qgis-ltr.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\qgis-ltr.bat qgis-ltr.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove saga-ltr.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\saga-ltr.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\saga-ltr.bat saga-ltr.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove setup.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\setup.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\setup.bat setup.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove shell.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\shell.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\shell.bat shell.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
echo Running preremove sip-qt5.bat...>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
%COMSPEC% /c etc\preremove\sip-qt5.bat>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren etc\preremove\sip-qt5.bat sip-qt5.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
ren preremove.bat preremove.bat.done>>%TEMP%\QGIS-OSGeo4W-3.16.11-1-preremove.log 2>&1
