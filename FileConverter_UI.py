# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileConverter_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileConverter_Window(object):
    def setupUi(self, FileConverter_Window):
        FileConverter_Window.setObjectName("FileConverter_Window")
        FileConverter_Window.resize(648, 539)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileConverter_Window.sizePolicy().hasHeightForWidth())
        FileConverter_Window.setSizePolicy(sizePolicy)
        FileConverter_Window.setStyleSheet("#FileConverter_Window{\n"
"background: qlineargradient(spread:pad,x1:0, y1:2, x2:1, y2:0,\n"
"                stop:0 #273641, stop:1 #39352f)\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(FileConverter_Window)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_bottom_app_desc = QtWidgets.QLabel(FileConverter_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bottom_app_desc.sizePolicy().hasHeightForWidth())
        self.label_bottom_app_desc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_bottom_app_desc.setFont(font)
        self.label_bottom_app_desc.setStyleSheet("color:white\n"
"")
        self.label_bottom_app_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_bottom_app_desc.setObjectName("label_bottom_app_desc")
        self.gridLayout_2.addWidget(self.label_bottom_app_desc, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SelectFile_btn = QtWidgets.QPushButton(FileConverter_Window)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.SelectFile_btn.setFont(font)
        self.SelectFile_btn.setStyleSheet("#SelectFile_btn{\n"
"background-color:#a0312f;\n"
"color:white;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"padding:2px;\n"
"}\n"
"#SelectFile_btn:hover{\n"
"background-color:#7a2624;\n"
"}\n"
"#SelectFile_btn:pressed{\n"
"border-style: inset;\n"
"background-color:#a0312f;\n"
"border:none\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SelectFile_btn.setIcon(icon)
        self.SelectFile_btn.setIconSize(QtCore.QSize(24, 24))
        self.SelectFile_btn.setObjectName("SelectFile_btn")
        self.horizontalLayout.addWidget(self.SelectFile_btn)
        self.Convert_btn = QtWidgets.QPushButton(FileConverter_Window)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.Convert_btn.setFont(font)
        self.Convert_btn.setStyleSheet("#Convert_btn{\n"
"background-color:#a0312f;\n"
"color:white;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"padding:2px;\n"
"}\n"
"#Convert_btn:hover{\n"
"background-color:#7a2624;\n"
"}\n"
"#Convert_btn:pressed{\n"
"border-style: inset;\n"
"background-color:#a0312f;\n"
"border:none\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Convert_btn.setIcon(icon1)
        self.Convert_btn.setIconSize(QtCore.QSize(24, 24))
        self.Convert_btn.setObjectName("Convert_btn")
        self.horizontalLayout.addWidget(self.Convert_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.frame_upper = QtWidgets.QFrame(FileConverter_Window)
        self.frame_upper.setAcceptDrops(False)
        self.frame_upper.setStyleSheet("#frame_upper{\n"
"background: qlineargradient(x1:1, y1:2, x2:0, y2:1,\n"
"                stop:0 #1a1c1d, stop:1 #2a2c2e);\n"
"}\n"
"QLabel{color:white;}")
        self.frame_upper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_upper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upper.setLineWidth(1)
        self.frame_upper.setMidLineWidth(0)
        self.frame_upper.setObjectName("frame_upper")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_upper)
        self.gridLayout.setContentsMargins(-1, 0, 9, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_title = QtWidgets.QLabel(self.frame_upper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setStyleSheet("#label{\n"
"color:white;\n"
"}")
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_title.setWordWrap(False)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 1, 1, 1)
        self.label_to = QtWidgets.QLabel(self.frame_upper)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_to.setFont(font)
        self.label_to.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_to.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_to.setObjectName("label_to")
        self.gridLayout.addWidget(self.label_to, 2, 5, 1, 1)
        self.comboBox_to = QtWidgets.QComboBox(self.frame_upper)
        self.comboBox_to.setObjectName("comboBox_to")
        self.gridLayout.addWidget(self.comboBox_to, 2, 6, 1, 1)
        self.comboBox_convert = QtWidgets.QComboBox(self.frame_upper)
        self.comboBox_convert.setObjectName("comboBox_convert")
        self.gridLayout.addWidget(self.comboBox_convert, 2, 4, 1, 1)
        self.label_convert = QtWidgets.QLabel(self.frame_upper)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_convert.setFont(font)
        self.label_convert.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_convert.setObjectName("label_convert")
        self.gridLayout.addWidget(self.label_convert, 2, 3, 1, 1)
        self.label_logo_image = QtWidgets.QLabel(self.frame_upper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo_image.sizePolicy().hasHeightForWidth())
        self.label_logo_image.setSizePolicy(sizePolicy)
        self.label_logo_image.setText("")
        self.label_logo_image.setPixmap(QtGui.QPixmap("icons/convert.png"))
        self.label_logo_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo_image.setObjectName("label_logo_image")
        self.gridLayout.addWidget(self.label_logo_image, 0, 0, 1, 1)
        self.label_description = QtWidgets.QLabel(self.frame_upper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setMinimumSize(QtCore.QSize(0, 0))
        self.label_description.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.label_description.setFont(font)
        self.label_description.setScaledContents(False)
        self.label_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")
        self.gridLayout.addWidget(self.label_description, 2, 0, 1, 2)
        self.Github_btn = QtWidgets.QPushButton(self.frame_upper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Github_btn.sizePolicy().hasHeightForWidth())
        self.Github_btn.setSizePolicy(sizePolicy)
        self.Github_btn.setStyleSheet("#Github_btn{\n"
"background-color:#34373a;\n"
"}")
        self.Github_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Github_btn.setIcon(icon2)
        self.Github_btn.setIconSize(QtCore.QSize(32, 32))
        self.Github_btn.setObjectName("Github_btn")
        self.gridLayout.addWidget(self.Github_btn, 0, 6, 1, 1)
        self.gridLayout_2.addWidget(self.frame_upper, 1, 0, 1, 1)
        self.label_update_type_desc = QtWidgets.QLabel(FileConverter_Window)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_update_type_desc.setFont(font)
        self.label_update_type_desc.setStyleSheet("color:white\n"
"")
        self.label_update_type_desc.setText("")
        self.label_update_type_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_update_type_desc.setWordWrap(True)
        self.label_update_type_desc.setObjectName("label_update_type_desc")
        self.gridLayout_2.addWidget(self.label_update_type_desc, 3, 0, 1, 1)

        self.retranslateUi(FileConverter_Window)
        QtCore.QMetaObject.connectSlotsByName(FileConverter_Window)

    def retranslateUi(self, FileConverter_Window):
        _translate = QtCore.QCoreApplication.translate
        FileConverter_Window.setWindowTitle(_translate("FileConverter_Window", "Form"))
        self.label_bottom_app_desc.setText(_translate("FileConverter_Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Other Apps:</span></p><p><span style=\" font-size:11pt;\">⚙AmazeX Utility</span></p><p><span style=\" font-size:11pt;\">🧮AKM Download Sorter</span></p><p><span style=\" font-size:11pt;\">🔹 AmazeX AHK</span></p><p align=\"right\"><span style=\" font-size:11pt;\">Developed By: EliteFantasy</span></p></body></html>"))
        self.SelectFile_btn.setText(_translate("FileConverter_Window", " Select File   "))
        self.Convert_btn.setText(_translate("FileConverter_Window", "  Convert     "))
        self.label_title.setText(_translate("FileConverter_Window", "File Converter"))
        self.label_to.setText(_translate("FileConverter_Window", "to"))
        self.label_convert.setText(_translate("FileConverter_Window", "convert"))
        self.label_description.setText(_translate("FileConverter_Window", "File Converter is an offline file converter We support image Formats(few) More Will be Added Soon. To get started use the button below and select files to convert from your computer."))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileConverter_Window = QtWidgets.QWidget()
    ui = Ui_FileConverter_Window()
    ui.setupUi(FileConverter_Window)
    FileConverter_Window.show()
    sys.exit(app.exec_())