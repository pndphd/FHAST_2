# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgCancelTaskQuery.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgCancelTaskQuery(object):
    def setupUi(self, DlgCancelTaskQuery):
        DlgCancelTaskQuery.setObjectName("DlgCancelTaskQuery")
        DlgCancelTaskQuery.resize(178, 101)
        DlgCancelTaskQuery.setWindowTitle("Dialog")
        self.verticalLayoutWidget = QtWidgets.QWidget(DlgCancelTaskQuery)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 168, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mLabel.setObjectName("mLabel")
        self.horizontalLayout.addWidget(self.mLabel)
        self.mMovie = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mMovie.setText("")
        self.mMovie.setObjectName("mMovie")
        self.horizontalLayout.addWidget(self.mMovie)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.mCancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mCancelButton.setObjectName("mCancelButton")
        self.horizontalLayout_2.addWidget(self.mCancelButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DlgCancelTaskQuery)
        QtCore.QMetaObject.connectSlotsByName(DlgCancelTaskQuery)

    def retranslateUi(self, DlgCancelTaskQuery):
        _translate = QtCore.QCoreApplication.translate
        self.mLabel.setText(_translate("DlgCancelTaskQuery", "Executing SQL…"))
        self.mCancelButton.setText(_translate("DlgCancelTaskQuery", "Cancel"))

