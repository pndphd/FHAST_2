# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugininstallerpluginerrorbase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsPluginInstallerPluginErrorDialogBase(object):
    def setupUi(self, QgsPluginInstallerPluginErrorDialogBase):
        QgsPluginInstallerPluginErrorDialogBase.setObjectName("QgsPluginInstallerPluginErrorDialogBase")
        QgsPluginInstallerPluginErrorDialogBase.resize(521, 383)
        QgsPluginInstallerPluginErrorDialogBase.setMinimumSize(QtCore.QSize(480, 300))
        self.gridlayout = QtWidgets.QGridLayout(QgsPluginInstallerPluginErrorDialogBase)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(QgsPluginInstallerPluginErrorDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(QgsPluginInstallerPluginErrorDialogBase)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setObjectName("textBrowser")
        self.gridlayout.addWidget(self.textBrowser, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(503, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(QgsPluginInstallerPluginErrorDialogBase)
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.gridlayout.addWidget(self.label1, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QgsPluginInstallerPluginErrorDialogBase)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem1, 0, 0, 1, 1)

        self.retranslateUi(QgsPluginInstallerPluginErrorDialogBase)
        self.buttonBox.rejected.connect(QgsPluginInstallerPluginErrorDialogBase.reject)
        self.buttonBox.accepted.connect(QgsPluginInstallerPluginErrorDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginInstallerPluginErrorDialogBase)

    def retranslateUi(self, QgsPluginInstallerPluginErrorDialogBase):
        _translate = QtCore.QCoreApplication.translate
        QgsPluginInstallerPluginErrorDialogBase.setWindowTitle(_translate("QgsPluginInstallerPluginErrorDialogBase", "Error loading plugin"))
        self.label.setText(_translate("QgsPluginInstallerPluginErrorDialogBase", "The plugin seems to be invalid or have unfulfilled dependencies. It has been installed, but can\'t be loaded. If you really need this plugin, you can contact its author or <a href=\"http://lists.osgeo.org/mailman/listinfo/qgis-user\">QGIS users group</a> and try to solve the problem. If not, you can just uninstall it. Here is the error message below:"))
        self.label1.setText(_translate("QgsPluginInstallerPluginErrorDialogBase", "Do you want to uninstall this plugin now? If you\'re unsure, probably you would like to do this."))

