# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/pyplugin_installer/qgsplugininstallerfetchingbase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsPluginInstallerFetchingDialogBase(object):
    def setupUi(self, QgsPluginInstallerFetchingDialogBase):
        QgsPluginInstallerFetchingDialogBase.setObjectName("QgsPluginInstallerFetchingDialogBase")
        QgsPluginInstallerFetchingDialogBase.resize(521, 332)
        self.gridlayout = QtWidgets.QGridLayout(QgsPluginInstallerFetchingDialogBase)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(249, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(QgsPluginInstallerFetchingDialogBase)
        self.label1.setObjectName("label1")
        self.gridlayout.addWidget(self.label1, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(QgsPluginInstallerFetchingDialogBase)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridlayout.addWidget(self.progressBar, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(248, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem2 = QtWidgets.QSpacerItem(140, 27, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.buttonSkip = QtWidgets.QPushButton(QgsPluginInstallerFetchingDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSkip.sizePolicy().hasHeightForWidth())
        self.buttonSkip.setSizePolicy(sizePolicy)
        self.buttonSkip.setMinimumSize(QtCore.QSize(180, 0))
        self.buttonSkip.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonSkip.setAutoDefault(False)
        self.buttonSkip.setDefault(False)
        self.buttonSkip.setFlat(False)
        self.buttonSkip.setObjectName("buttonSkip")
        self.hboxlayout.addWidget(self.buttonSkip)
        spacerItem3 = QtWidgets.QSpacerItem(140, 27, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.gridlayout.addLayout(self.hboxlayout, 5, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(QgsPluginInstallerFetchingDialogBase)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setObjectName("treeWidget")
        self.gridlayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.retranslateUi(QgsPluginInstallerFetchingDialogBase)
        self.buttonSkip.clicked.connect(QgsPluginInstallerFetchingDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QgsPluginInstallerFetchingDialogBase)

    def retranslateUi(self, QgsPluginInstallerFetchingDialogBase):
        _translate = QtCore.QCoreApplication.translate
        QgsPluginInstallerFetchingDialogBase.setWindowTitle(_translate("QgsPluginInstallerFetchingDialogBase", "Fetching repositories"))
        self.label1.setText(_translate("QgsPluginInstallerFetchingDialogBase", "Overall progress"))
        self.buttonSkip.setText(_translate("QgsPluginInstallerFetchingDialogBase", "Abort Fetching"))
        self.treeWidget.headerItem().setText(0, _translate("QgsPluginInstallerFetchingDialogBase", "Repository"))
        self.treeWidget.headerItem().setText(1, _translate("QgsPluginInstallerFetchingDialogBase", "State"))

