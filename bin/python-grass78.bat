@echo off
rem #########################################################################
rem #
rem # GRASS initialization bat script for Python environment (OSGeo4W)
rem #
rem #########################################################################

rem
rem Set environmental variables
rem
call "%~dp0\o4w_env.bat"
call "%OSGEO4W_ROOT%\apps\grass\grass78\etc\env.bat"
@echo off

set PYTHONPATH=%OSGEO4W_ROOT%\apps\grass\grass78\etc\python;%PYTHONPATH%
"%GRASS_PYTHON%" %*

rem
rem Pause on error
rem
if %ERRORLEVEL% GEQ 1 pause
