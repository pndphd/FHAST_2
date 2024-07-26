# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/console/console_history_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistoryDialogPythonConsole(object):
    def setupUi(self, HistoryDialogPythonConsole):
        HistoryDialogPythonConsole.setObjectName("HistoryDialogPythonConsole")
        HistoryDialogPythonConsole.resize(587, 375)
        HistoryDialogPythonConsole.setWindowTitle("Dialog")
        self.gridLayout = QtWidgets.QGridLayout(HistoryDialogPythonConsole)
        self.gridLayout.setContentsMargins(2, 4, 2, 4)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(HistoryDialogPythonConsole)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)
        self.listView = QtWidgets.QListView(HistoryDialogPythonConsole)
        self.listView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 3)
        self.reloadHistory = QtWidgets.QPushButton(HistoryDialogPythonConsole)
        self.reloadHistory.setObjectName("reloadHistory")
        self.gridLayout.addWidget(self.reloadHistory, 2, 0, 1, 1)
        self.saveHistory = QtWidgets.QPushButton(HistoryDialogPythonConsole)
        self.saveHistory.setEnabled(True)
        self.saveHistory.setObjectName("saveHistory")
        self.gridLayout.addWidget(self.saveHistory, 2, 1, 1, 1)

        self.retranslateUi(HistoryDialogPythonConsole)
        self.buttonBox.accepted.connect(HistoryDialogPythonConsole.accept)
        self.buttonBox.rejected.connect(HistoryDialogPythonConsole.reject)
        QtCore.QMetaObject.connectSlotsByName(HistoryDialogPythonConsole)

    def retranslateUi(self, HistoryDialogPythonConsole):
        _translate = QtCore.QCoreApplication.translate
        self.reloadHistory.setText(_translate("HistoryDialogPythonConsole", "Reload"))
        self.saveHistory.setText(_translate("HistoryDialogPythonConsole", "Save"))

