# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\JetBrains-code\Python\qt5\xml\WeChat.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(925, 557)
        mainWindow.setMinimumSize(QtCore.QSize(925, 557))
        mainWindow.setMaximumSize(QtCore.QSize(935, 557))
        mainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        mainWindow.setDocumentMode(True)
        mainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 711, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 390, 711, 101))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(550, 500, 184, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButtonSend = QtWidgets.QPushButton(self.splitter)
        self.pushButtonSend.setDefault(False)
        self.pushButtonSend.setFlat(False)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.pushButtonExit = QtWidgets.QPushButton(self.splitter)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 360, 167, 21))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.toolButton = QtWidgets.QToolButton(self.splitter_2)
        self.toolButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.toolButton.setObjectName("toolButton")
        self.fontComboBox = QtWidgets.QFontComboBox(self.splitter_2)
        self.fontComboBox.setObjectName("fontComboBox")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(mainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(172, 532))
        self.dockWidget.setMaximumSize(QtCore.QSize(172, 532))
        self.dockWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dockWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dockWidget.setWindowTitle("")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 151, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("f:\\JetBrains-code\\Python\\qt5\\xml\\../img/Avatar_1.png"))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 151, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "WeChat"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.pushButtonSend.setText(_translate("mainWindow", "send"))
        self.pushButtonExit.setText(_translate("mainWindow", "exit"))
        self.toolButton.setText(_translate("mainWindow", "emoj"))
        self.fontComboBox.setCurrentText(_translate("mainWindow", "字体选择"))
