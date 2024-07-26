# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/console/console_compile_apis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_APIsDialogPythonConsole(object):
    def setupUi(self, APIsDialogPythonConsole):
        APIsDialogPythonConsole.setObjectName("APIsDialogPythonConsole")
        APIsDialogPythonConsole.resize(320, 280)
        APIsDialogPythonConsole.setMinimumSize(QtCore.QSize(320, 0))
        APIsDialogPythonConsole.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(APIsDialogPythonConsole)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(APIsDialogPythonConsole)
        self.label.setMinimumSize(QtCore.QSize(320, 0))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(APIsDialogPythonConsole)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(APIsDialogPythonConsole)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.textEdit_Qsci = Qsci.QsciScintilla(APIsDialogPythonConsole)
        self.textEdit_Qsci.setToolTip("")
        self.textEdit_Qsci.setWhatsThis("")
        self.textEdit_Qsci.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_Qsci.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_Qsci.setObjectName("textEdit_Qsci")
        self.verticalLayout.addWidget(self.textEdit_Qsci)
        self.buttonBox = QtWidgets.QDialogButtonBox(APIsDialogPythonConsole)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(APIsDialogPythonConsole)
        QtCore.QMetaObject.connectSlotsByName(APIsDialogPythonConsole)

    def retranslateUi(self, APIsDialogPythonConsole):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("APIsDialogPythonConsole", "Generating prepared API file (please wait)…"))

from PyQt5 import Qsci
