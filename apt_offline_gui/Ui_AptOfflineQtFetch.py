# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtFetch.ui'
#
# Created: Sat Feb 19 21:24:01 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AptOfflineQtFetch(object):
    def setupUi(self, AptOfflineQtFetch):
        AptOfflineQtFetch.setObjectName("AptOfflineQtFetch")
        AptOfflineQtFetch.setWindowModality(QtCore.Qt.ApplicationModal)
        AptOfflineQtFetch.resize(468, 483)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AptOfflineQtFetch.sizePolicy().hasHeightForWidth())
        AptOfflineQtFetch.setSizePolicy(sizePolicy)
        AptOfflineQtFetch.setMinimumSize(QtCore.QSize(468, 475))
        AptOfflineQtFetch.setMaximumSize(QtCore.QSize(468, 495))
        self.profileFilePath = QtGui.QLineEdit(AptOfflineQtFetch)
        self.profileFilePath.setGeometry(QtCore.QRect(30, 35, 270, 30))
        self.profileFilePath.setObjectName("profileFilePath")
        self.browseFilePathButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.browseFilePathButton.setGeometry(QtCore.QRect(320, 35, 110, 30))
        self.browseFilePathButton.setObjectName("browseFilePathButton")
        self.startDownloadButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.startDownloadButton.setEnabled(False)
        self.startDownloadButton.setGeometry(QtCore.QRect(179, 148, 120, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startDownloadButton.setIcon(icon)
        self.startDownloadButton.setShortcut("None")
        self.startDownloadButton.setCheckable(False)
        self.startDownloadButton.setChecked(False)
        self.startDownloadButton.setFlat(False)
        self.startDownloadButton.setObjectName("startDownloadButton")
        self.cancelButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.cancelButton.setGeometry(QtCore.QRect(319, 148, 111, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName("cancelButton")
        self.lblSelectSig = QtGui.QLabel(AptOfflineQtFetch)
        self.lblSelectSig.setGeometry(QtCore.QRect(30, 5, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSelectSig.setFont(font)
        self.lblSelectSig.setObjectName("lblSelectSig")
        self.statusProgressBar = QtGui.QProgressBar(AptOfflineQtFetch)
        self.statusProgressBar.setGeometry(QtCore.QRect(30, 214, 410, 20))
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setObjectName("statusProgressBar")
        self.lblStatus = QtGui.QLabel(AptOfflineQtFetch)
        self.lblStatus.setGeometry(QtCore.QRect(32, 194, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblStatus.setFont(font)
        self.lblStatus.setObjectName("lblStatus")
        self.progressStatusDescription = QtGui.QLabel(AptOfflineQtFetch)
        self.progressStatusDescription.setGeometry(QtCore.QRect(82, 194, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressStatusDescription.setFont(font)
        self.progressStatusDescription.setObjectName("progressStatusDescription")
        self.rawLogHolder = QtGui.QTextEdit(AptOfflineQtFetch)
        self.rawLogHolder.setGeometry(QtCore.QRect(30, 252, 411, 211))
        self.rawLogHolder.setObjectName("rawLogHolder")
        self.browseZipFileButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.browseZipFileButton.setGeometry(QtCore.QRect(320, 98, 110, 30))
        self.browseZipFileButton.setObjectName("browseZipFileButton")
        self.lblSaveAs = QtGui.QLabel(AptOfflineQtFetch)
        self.lblSaveAs.setGeometry(QtCore.QRect(30, 68, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSaveAs.setFont(font)
        self.lblSaveAs.setObjectName("lblSaveAs")
        self.zipFilePath = QtGui.QLineEdit(AptOfflineQtFetch)
        self.zipFilePath.setGeometry(QtCore.QRect(30, 98, 270, 30))
        self.zipFilePath.setObjectName("zipFilePath")
        self.spinThreads = QtGui.QSpinBox(AptOfflineQtFetch)
        self.spinThreads.setGeometry(QtCore.QRect(122, 148, 40, 30))
        self.spinThreads.setMinimum(1)
        self.spinThreads.setMaximum(10)
        self.spinThreads.setObjectName("spinThreads")
        self.lblThreads = QtGui.QLabel(AptOfflineQtFetch)
        self.lblThreads.setGeometry(QtCore.QRect(32, 149, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblThreads.setFont(font)
        self.lblThreads.setObjectName("lblThreads")

        self.retranslateUi(AptOfflineQtFetch)
        QtCore.QMetaObject.connectSlotsByName(AptOfflineQtFetch)

    def retranslateUi(self, AptOfflineQtFetch):
        AptOfflineQtFetch.setWindowTitle(QtGui.QApplication.translate("AptOfflineQtFetch", "Fetch Packages or Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.browseFilePathButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.startDownloadButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSelectSig.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Select the signature file", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.progressStatusDescription.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.browseZipFileButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSaveAs.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Save archive as", None, QtGui.QApplication.UnicodeUTF8))
        self.lblThreads.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Use threads", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
