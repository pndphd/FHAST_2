del apps/Python37/Scripts/easy_install-3.7.exe
del apps/Python37/Scripts/easy_install.exe
call %OSGEO4W_ROOT%\bin\py3_env.bat
python -B %PYTHONHOME%\Scripts\preremove-cached.py python3-setuptools
