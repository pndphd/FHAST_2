# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FHASTLoader
                                 A QGIS plugin
 Loads a set of user selected files for a FHAST run
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-05-31
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Peter Dudley
        email                : pndphd@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QApplication 


# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .fhast_loader_dialog import FHASTLoaderDialog
import os.path

class FHASTLoader:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'FHASTLoader_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&FHAST Loader')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('FHASTLoader', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)
     
        menu_buttons = self.iface.mainWindow().menuBar().actions()
        button_list = []

        for button in menu_buttons:
            button_list.append(button.text())

        new_button = '&FHAST'

        self.menu = self.iface.mainWindow().findChild(QMenu, '&FHAST' )

        if not new_button in button_list:
        # # If the menu does not exist, create it!
            self.menu = QMenu( new_button, self.iface.mainWindow().menuBar() )
            self.menu.setObjectName( new_button )
            actions = self.iface.mainWindow().menuBar().actions()
            lastAction = actions[-1]
            self.iface.mainWindow().menuBar().insertMenu( lastAction, self.menu )

        # Finally, add your action to the menu
        self.menu.addAction(action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/fhast_loader/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'FHAST File Loader'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&FHAST Loader'),
                action)
            self.iface.removeToolBarIcon(action)

            
    def run(self):
        """Run method that performs all the real work"""
        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
        # moved out out of loop so resets fields
        self.dlg = FHASTLoaderDialog()

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Get the lkayer tree to get group names
            root = QgsProject.instance().layerTreeRoot()
            root_groups = root.findGroups()
            # Make a list of all group names and add any missing
            group_list = []
            for group_name in root_groups:
                group_list.append(group_name.name())

            needed_groups = ["Grid Centerline",
                             "Grid Top Point",
                             "Area of Interest (Optional)",
                             "Cover File",
                             "Wildcard File (Optional)",
                             "Canopy File",
                             "Tree Growth",
                             "Depth or Velocity Example Raster",
                             "Environmental Input File",
                             "Fish Population File",
                             "Fish Parameters File",
                             "Predator Parameters File",
                             "Habitat Parameters File",
                             "Interactions Parameters File"]

            for needed_group in needed_groups:
                if not needed_group in group_list:
                    myGroup1 = root.addGroup(needed_group)

            # get all the variables for shape files 
            grid_cl_file = QgsVectorLayer(self.dlg.grid_centerline.filePath(), "centerline_shp", "ogr")
            grid_tp_file = QgsVectorLayer(self.dlg.grid_top_point.filePath(), "toppoint_shp", "ogr")
            aoi_file = QgsVectorLayer(self.dlg.aoi.filePath(), "aoi_shp", "ogr")
            cover_shape_file = QgsVectorLayer(self.dlg.cover_file.filePath(), "cover_shp", "ogr")
            canopy_shape_file = QgsVectorLayer(self.dlg.canopy_file.filePath(), "canopy_shp", "ogr")
            eg_flow_file = QgsRasterLayer(self.dlg.flow_file.filePath(), "flow_raster")
            
            # get all the variables for shape files 
            wildcard_file = QgsVectorLayer(self.dlg.wildcard.filePath(), "wildcard_table", "ogr")
            tg_file = QgsVectorLayer(self.dlg.tree_growth.filePath(), "tg_table", "ogr")
            daily_con_file = QgsVectorLayer(self.dlg.daily_conditions_file.filePath(), "daily_table", "ogr")
            fish_pop_file = QgsVectorLayer(self.dlg.fish_population_file.filePath(), "fish_pop_table", "ogr")
            fish_param_file = QgsVectorLayer(self.dlg.fish_parameters_file.filePath(), "fish_param_table", "ogr")
            pred_param_file = QgsVectorLayer(self.dlg.predator_parameters_file.filePath(), "pred_param_table", "ogr")
            habitat_param_file = QgsVectorLayer(self.dlg.habitat_parameters_file.filePath(), "habitat_table", "ogr")
            int_param_file = QgsVectorLayer(self.dlg.interactions_parameters_file.filePath(), "int_table", "ogr")

            for group in root.findGroups():
                if (group.name() == "Canopy File"):
                    if (canopy_shape_file.isValid()):
                        QgsProject.instance().addMapLayer(canopy_shape_file)
                        layer = root.findLayer(canopy_shape_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Fish Population File"):
                    if (fish_pop_file.isValid()):
                        QgsProject.instance().addMapLayer(fish_pop_file)
                        layer = root.findLayer(fish_pop_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Grid Centerline"):
                    if (grid_cl_file.isValid()):
                        QgsProject.instance().addMapLayer(grid_cl_file)
                        layer = root.findLayer(grid_cl_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Grid Top Point"):
                    if (grid_tp_file.isValid()):
                        QgsProject.instance().addMapLayer(grid_tp_file)
                        layer = root.findLayer(grid_tp_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Area of Interest (Optional)"):
                    if (aoi_file.isValid()):
                        QgsProject.instance().addMapLayer(aoi_file)
                        layer = root.findLayer(aoi_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Wildcard File (Optional)"):
                    if (wildcard_file.isValid()):
                        QgsProject.instance().addMapLayer(wildcard_file)
                        layer = root.findLayer(wildcard_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Tree Growth"):
                    if (tg_file.isValid()):
                        QgsProject.instance().addMapLayer(tg_file)
                        layer = root.findLayer(tg_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Depth or Velocity Example Raster"):
                    if (eg_flow_file.isValid()):
                        QgsProject.instance().addMapLayer(eg_flow_file)
                        layer = root.findLayer(eg_flow_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Environmental Input File"):
                    if (daily_con_file.isValid()):
                        QgsProject.instance().addMapLayer(daily_con_file)
                        layer = root.findLayer(daily_con_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Fish Parameters File"):
                    if (fish_param_file.isValid()):
                        QgsProject.instance().addMapLayer(fish_param_file)
                        layer = root.findLayer(fish_param_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Predator Parameters File"):
                    if (pred_param_file.isValid()):
                        QgsProject.instance().addMapLayer(pred_param_file)
                        layer = root.findLayer(pred_param_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Habitat Parameters File"):
                    if (habitat_param_file.isValid()):
                        QgsProject.instance().addMapLayer(habitat_param_file)
                        layer = root.findLayer(habitat_param_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Interactions Parameters File"):
                    if (int_param_file.isValid()):
                        QgsProject.instance().addMapLayer(int_param_file)
                        layer = root.findLayer(int_param_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)
                if (group.name() == "Cover File"):
                    if (cover_shape_file.isValid()):
                        QgsProject.instance().addMapLayer(cover_shape_file)
                        layer = root.findLayer(cover_shape_file.id())
                        clone = layer.clone()
                        group.insertChildNode(0, clone)
                        layer.parent().removeChildNode(layer)



        

