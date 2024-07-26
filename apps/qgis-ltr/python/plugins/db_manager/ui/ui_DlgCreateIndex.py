# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgCreateIndex.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbManagerDlgCreateIndex(object):
    def setupUi(self, DbManagerDlgCreateIndex):
        DbManagerDlgCreateIndex.setObjectName("DbManagerDlgCreateIndex")
        DbManagerDlgCreateIndex.resize(357, 111)
        self.gridlayout = QtWidgets.QGridLayout(DbManagerDlgCreateIndex)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(DbManagerDlgCreateIndex)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.cboColumn = QtWidgets.QComboBox(DbManagerDlgCreateIndex)
        self.cboColumn.setObjectName("cboColumn")
        self.gridlayout.addWidget(self.cboColumn, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DbManagerDlgCreateIndex)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(DbManagerDlgCreateIndex)
        self.editName.setText("")
        self.editName.setObjectName("editName")
        self.gridlayout.addWidget(self.editName, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DbManagerDlgCreateIndex)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(DbManagerDlgCreateIndex)
        self.buttonBox.rejected.connect(DbManagerDlgCreateIndex.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgCreateIndex)
        DbManagerDlgCreateIndex.setTabOrder(self.cboColumn, self.editName)
        DbManagerDlgCreateIndex.setTabOrder(self.editName, self.buttonBox)

    def retranslateUi(self, DbManagerDlgCreateIndex):
        _translate = QtCore.QCoreApplication.translate
        DbManagerDlgCreateIndex.setWindowTitle(_translate("DbManagerDlgCreateIndex", "Create index"))
        self.label.setText(_translate("DbManagerDlgCreateIndex", "Column"))
        self.label_2.setText(_translate("DbManagerDlgCreateIndex", "Name"))

