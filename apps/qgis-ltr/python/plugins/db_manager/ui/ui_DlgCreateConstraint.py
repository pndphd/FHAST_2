# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgCreateConstraint.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbManagerDlgCreateConstraint(object):
    def setupUi(self, DbManagerDlgCreateConstraint):
        DbManagerDlgCreateConstraint.setObjectName("DbManagerDlgCreateConstraint")
        DbManagerDlgCreateConstraint.resize(284, 138)
        self.gridLayout = QtWidgets.QGridLayout(DbManagerDlgCreateConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DbManagerDlgCreateConstraint)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cboColumn = QtWidgets.QComboBox(DbManagerDlgCreateConstraint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboColumn.sizePolicy().hasHeightForWidth())
        self.cboColumn.setSizePolicy(sizePolicy)
        self.cboColumn.setObjectName("cboColumn")
        self.gridLayout.addWidget(self.cboColumn, 0, 1, 1, 1)
        self.radPrimaryKey = QtWidgets.QRadioButton(DbManagerDlgCreateConstraint)
        self.radPrimaryKey.setChecked(True)
        self.radPrimaryKey.setObjectName("radPrimaryKey")
        self.gridLayout.addWidget(self.radPrimaryKey, 1, 1, 1, 1)
        self.radUnique = QtWidgets.QRadioButton(DbManagerDlgCreateConstraint)
        self.radUnique.setObjectName("radUnique")
        self.gridLayout.addWidget(self.radUnique, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DbManagerDlgCreateConstraint)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(DbManagerDlgCreateConstraint)
        self.buttonBox.rejected.connect(DbManagerDlgCreateConstraint.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgCreateConstraint)

    def retranslateUi(self, DbManagerDlgCreateConstraint):
        _translate = QtCore.QCoreApplication.translate
        DbManagerDlgCreateConstraint.setWindowTitle(_translate("DbManagerDlgCreateConstraint", "Add constraint"))
        self.label.setText(_translate("DbManagerDlgCreateConstraint", "Column"))
        self.radPrimaryKey.setText(_translate("DbManagerDlgCreateConstraint", "Primary key"))
        self.radUnique.setText(_translate("DbManagerDlgCreateConstraint", "Unique"))

