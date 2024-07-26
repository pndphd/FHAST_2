set OSGEO4W_ROOT=%OSGEO4W_ROOT:\=\\%
textreplace -std -t apps\Python37\Scripts\pyuic5.bat
textreplace -std -t apps\Python37\Scripts\pyrcc5.bat
textreplace -std -t apps\Python37\Scripts\pylupdate5.bat
