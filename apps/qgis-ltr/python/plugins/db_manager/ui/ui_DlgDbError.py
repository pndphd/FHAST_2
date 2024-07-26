# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/db_manager/ui/DlgDbError.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbManagerDlgDbError(object):
    def setupUi(self, DbManagerDlgDbError):
        DbManagerDlgDbError.setObjectName("DbManagerDlgDbError")
        DbManagerDlgDbError.resize(400, 314)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DbManagerDlgDbError)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(DbManagerDlgDbError)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.txtErrorMsg = QtWidgets.QTextBrowser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtErrorMsg.sizePolicy().hasHeightForWidth())
        self.txtErrorMsg.setSizePolicy(sizePolicy)
        self.txtErrorMsg.setObjectName("txtErrorMsg")
        self.verticalLayout_3.addWidget(self.txtErrorMsg)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtQueryErrorMsg = QtWidgets.QTextBrowser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtQueryErrorMsg.sizePolicy().hasHeightForWidth())
        self.txtQueryErrorMsg.setSizePolicy(sizePolicy)
        self.txtQueryErrorMsg.setObjectName("txtQueryErrorMsg")
        self.verticalLayout.addWidget(self.txtQueryErrorMsg)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txtQuery = QtWidgets.QTextBrowser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.txtQuery.sizePolicy().hasHeightForWidth())
        self.txtQuery.setSizePolicy(sizePolicy)
        self.txtQuery.setObjectName("txtQuery")
        self.verticalLayout.addWidget(self.txtQuery)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DbManagerDlgDbError)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DbManagerDlgDbError)
        self.stackedWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(DbManagerDlgDbError.accept)
        self.buttonBox.rejected.connect(DbManagerDlgDbError.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgDbError)

    def retranslateUi(self, DbManagerDlgDbError):
        _translate = QtCore.QCoreApplication.translate
        DbManagerDlgDbError.setWindowTitle(_translate("DbManagerDlgDbError", "Database Error"))
        self.label_3.setText(_translate("DbManagerDlgDbError", "An error occurred"))
        self.label.setText(_translate("DbManagerDlgDbError", "An error occurred when executing a query"))
        self.label_2.setText(_translate("DbManagerDlgDbError", "Query"))

