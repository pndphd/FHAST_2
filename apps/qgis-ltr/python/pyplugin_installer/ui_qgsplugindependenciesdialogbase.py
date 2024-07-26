# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugindependenciesdialogbase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsPluginDependenciesDialogBase(object):
    def setupUi(self, QgsPluginDependenciesDialogBase):
        QgsPluginDependenciesDialogBase.setObjectName("QgsPluginDependenciesDialogBase")
        QgsPluginDependenciesDialogBase.resize(1211, 437)
        QgsPluginDependenciesDialogBase.setWindowTitle("Dialog")
        self.verticalLayout = QtWidgets.QVBoxLayout(QgsPluginDependenciesDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mPluginDependenciesLabel = QtWidgets.QLabel(QgsPluginDependenciesDialogBase)
        self.mPluginDependenciesLabel.setObjectName("mPluginDependenciesLabel")
        self.verticalLayout.addWidget(self.mPluginDependenciesLabel)
        self.pluginList = QtWidgets.QTableWidget(QgsPluginDependenciesDialogBase)
        self.pluginList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pluginList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.pluginList.setObjectName("pluginList")
        self.pluginList.setColumnCount(0)
        self.pluginList.setRowCount(0)
        self.pluginList.horizontalHeader().setSortIndicatorShown(False)
        self.pluginList.horizontalHeader().setStretchLastSection(True)
        self.pluginList.verticalHeader().setVisible(False)
        self.pluginList.verticalHeader().setHighlightSections(False)
        self.pluginList.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.pluginList)
        self.buttonBox = QtWidgets.QDialogButtonBox(QgsPluginDependenciesDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QgsPluginDependenciesDialogBase)
        self.buttonBox.accepted.connect(QgsPluginDependenciesDialogBase.accept)
        self.buttonBox.rejected.connect(QgsPluginDependenciesDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginDependenciesDialogBase)

    def retranslateUi(self, QgsPluginDependenciesDialogBase):
        _translate = QtCore.QCoreApplication.translate
        self.mPluginDependenciesLabel.setText(_translate("QgsPluginDependenciesDialogBase", "Plugin dependencies"))

