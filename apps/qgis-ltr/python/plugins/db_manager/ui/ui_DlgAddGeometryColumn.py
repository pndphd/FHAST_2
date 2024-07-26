# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgAddGeometryColumn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbManagerDlgAddGeometryColumn(object):
    def setupUi(self, DbManagerDlgAddGeometryColumn):
        DbManagerDlgAddGeometryColumn.setObjectName("DbManagerDlgAddGeometryColumn")
        DbManagerDlgAddGeometryColumn.resize(297, 179)
        self.gridLayout = QtWidgets.QGridLayout(DbManagerDlgAddGeometryColumn)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DbManagerDlgAddGeometryColumn)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(DbManagerDlgAddGeometryColumn)
        self.editName.setText("geom")
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(DbManagerDlgAddGeometryColumn)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cboType = QtWidgets.QComboBox(DbManagerDlgAddGeometryColumn)
        self.cboType.setObjectName("cboType")
        self.cboType.addItem("")
        self.cboType.setItemText(0, "POINT")
        self.cboType.addItem("")
        self.cboType.setItemText(1, "LINESTRING")
        self.cboType.addItem("")
        self.cboType.setItemText(2, "POLYGON")
        self.cboType.addItem("")
        self.cboType.setItemText(3, "MULTIPOINT")
        self.cboType.addItem("")
        self.cboType.setItemText(4, "MULTILINESTRING")
        self.cboType.addItem("")
        self.cboType.setItemText(5, "MULTIPOLYGON")
        self.cboType.addItem("")
        self.cboType.setItemText(6, "GEOMETRYCOLLECTION")
        self.gridLayout.addWidget(self.cboType, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(DbManagerDlgAddGeometryColumn)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinDim = QtWidgets.QSpinBox(DbManagerDlgAddGeometryColumn)
        self.spinDim.setMinimum(2)
        self.spinDim.setMaximum(4)
        self.spinDim.setObjectName("spinDim")
        self.gridLayout.addWidget(self.spinDim, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 2, 1)
        self.label_4 = QtWidgets.QLabel(DbManagerDlgAddGeometryColumn)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.editSrid = QtWidgets.QLineEdit(DbManagerDlgAddGeometryColumn)
        self.editSrid.setText("0")
        self.editSrid.setObjectName("editSrid")
        self.gridLayout.addWidget(self.editSrid, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DbManagerDlgAddGeometryColumn)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(DbManagerDlgAddGeometryColumn)
        self.buttonBox.rejected.connect(DbManagerDlgAddGeometryColumn.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgAddGeometryColumn)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.editName, self.cboType)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.cboType, self.spinDim)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.spinDim, self.editSrid)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.editSrid, self.buttonBox)

    def retranslateUi(self, DbManagerDlgAddGeometryColumn):
        _translate = QtCore.QCoreApplication.translate
        DbManagerDlgAddGeometryColumn.setWindowTitle(_translate("DbManagerDlgAddGeometryColumn", "Add geometry column"))
        self.label.setText(_translate("DbManagerDlgAddGeometryColumn", "Name"))
        self.label_2.setText(_translate("DbManagerDlgAddGeometryColumn", "Type"))
        self.label_3.setText(_translate("DbManagerDlgAddGeometryColumn", "Dimensions"))
        self.label_4.setText(_translate("DbManagerDlgAddGeometryColumn", "SRID"))

