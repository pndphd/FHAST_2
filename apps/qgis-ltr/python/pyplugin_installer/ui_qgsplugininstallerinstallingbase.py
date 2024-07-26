# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugininstallerinstallingbase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsPluginInstallerInstallingDialogBase(object):
    def setupUi(self, QgsPluginInstallerInstallingDialogBase):
        QgsPluginInstallerInstallingDialogBase.setObjectName("QgsPluginInstallerInstallingDialogBase")
        QgsPluginInstallerInstallingDialogBase.resize(520, 175)
        self.gridlayout = QtWidgets.QGridLayout(QgsPluginInstallerInstallingDialogBase)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(502, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridlayout.addItem(spacerItem, 0, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtWidgets.QLabel(QgsPluginInstallerInstallingDialogBase)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.labelName = QtWidgets.QLabel(QgsPluginInstallerInstallingDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.hboxlayout.addWidget(self.labelName)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.labelState = QtWidgets.QLabel(QgsPluginInstallerInstallingDialogBase)
        self.labelState.setObjectName("labelState")
        self.gridlayout.addWidget(self.labelState, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(QgsPluginInstallerInstallingDialogBase)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridlayout.addWidget(self.progressBar, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(502, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QgsPluginInstallerInstallingDialogBase)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(QgsPluginInstallerInstallingDialogBase)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginInstallerInstallingDialogBase)

    def retranslateUi(self, QgsPluginInstallerInstallingDialogBase):
        _translate = QtCore.QCoreApplication.translate
        QgsPluginInstallerInstallingDialogBase.setWindowTitle(_translate("QgsPluginInstallerInstallingDialogBase", "QGIS Python Plugin Installer"))
        self.label.setText(_translate("QgsPluginInstallerInstallingDialogBase", "Installing plugin:"))
        self.labelState.setText(_translate("QgsPluginInstallerInstallingDialogBase", "Connecting…"))

