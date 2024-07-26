del apps/Python37/Scripts/pip.exe
del apps/Python37/Scripts/pip3.7.exe
del apps/Python37/Scripts/pip3.exe
call %OSGEO4W_ROOT%\bin\py3_env.bat
python -B %PYTHONHOME%\Scripts\preremove-cached.py python3-pip
