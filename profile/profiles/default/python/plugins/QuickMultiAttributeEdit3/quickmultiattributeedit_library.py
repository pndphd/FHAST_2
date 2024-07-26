# --------------------------------------------------------
#    quickmultiattributeedit_library - quickmultiattributeedit operation functions
#
#    begin                : 10 May 2010
#    copyright            : (c) 2010 by Michael Minn
#    email                : See michaelminn.com
#
#   QuickMultiAttributeEdit is free software and is offered 
#   without guarantee or warranty. You can redistribute it 
#   and/or modify it under the terms of version 2 of the 
#   GNU General Public License (GPL v2) as published by the 
#   Free Software Foundation (www.gnu.org).
# --------------------------------------------------------

from future import standard_library
standard_library.install_aliases()
import csv
import time
import urllib.request, urllib.parse, urllib.error
import os.path
import operator

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from math import *


# --------------------------------------------------------
#    quickmultiattributeedit_update_selected - Update field of selected elements
# --------------------------------------------------------

def quickmultiattributeedit_update_selected():
    pass    


