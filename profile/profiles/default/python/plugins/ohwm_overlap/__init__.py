# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OHWMOverlap
                                 A QGIS plugin
 get intersection of OHWM and project 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-05-14
        copyright            : (C) 2025 by Peter Dudley
        email                : pndphd@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OHWMOverlap class from file OHWMOverlap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ohwm_overlap import OHWMOverlap
    return OHWMOverlap(iface)
