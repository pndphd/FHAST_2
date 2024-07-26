# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickmultiattributeedit_update_selected_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_quickmultiattributeedit_update_selected_form(object):
    def setupUi(self, quickmultiattributeedit_update_selected_form):
        quickmultiattributeedit_update_selected_form.setObjectName("quickmultiattributeedit_update_selected_form")
        quickmultiattributeedit_update_selected_form.resize(654, 164)
        self.buttonBox = QtWidgets.QDialogButtonBox(quickmultiattributeedit_update_selected_form)
        self.buttonBox.setGeometry(QtCore.QRect(360, 80, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.CBfields = QtWidgets.QComboBox(quickmultiattributeedit_update_selected_form)
        self.CBfields.setGeometry(QtCore.QRect(10, 40, 211, 24))
        self.CBfields.setObjectName("CBfields")
        self.QLEvalore = QtWidgets.QLineEdit(quickmultiattributeedit_update_selected_form)
        self.QLEvalore.setGeometry(QtCore.QRect(300, 40, 256, 24))
        self.QLEvalore.setObjectName("QLEvalore")
        self.label = QtWidgets.QLabel(quickmultiattributeedit_update_selected_form)
        self.label.setGeometry(QtCore.QRect(10, 10, 631, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(quickmultiattributeedit_update_selected_form)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 61, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(quickmultiattributeedit_update_selected_form)
        self.label_3.setGeometry(QtCore.QRect(10, 125, 631, 21))
        self.label_3.setObjectName("label_3")
        self.cBkeepLatestValue = QtWidgets.QCheckBox(quickmultiattributeedit_update_selected_form)
        self.cBkeepLatestValue.setGeometry(QtCore.QRect(20, 85, 211, 19))
        self.cBkeepLatestValue.setChecked(True)
        self.cBkeepLatestValue.setObjectName("cBkeepLatestValue")

        self.retranslateUi(quickmultiattributeedit_update_selected_form)
        self.buttonBox.accepted.connect(quickmultiattributeedit_update_selected_form.accept)
        self.buttonBox.rejected.connect(quickmultiattributeedit_update_selected_form.reject)
        QtCore.QMetaObject.connectSlotsByName(quickmultiattributeedit_update_selected_form)

    def retranslateUi(self, quickmultiattributeedit_update_selected_form):
        _translate = QtCore.QCoreApplication.translate
        quickmultiattributeedit_update_selected_form.setWindowTitle(_translate("quickmultiattributeedit_update_selected_form", "MBupSelected"))
        self.label.setText(_translate("quickmultiattributeedit_update_selected_form", "For all selected elements in the current layer set the value of field:"))
        self.label_2.setText(_translate("quickmultiattributeedit_update_selected_form", "equal to:"))
        self.label_3.setText(_translate("quickmultiattributeedit_update_selected_form", "F10 funct key shortcut to this dialog - by Marco Braida 2011"))
        self.cBkeepLatestValue.setText(_translate("quickmultiattributeedit_update_selected_form", "Keep latest input value"))

