# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_dialog(object):
    def setupUi(self, edit_dialog):
        edit_dialog.setObjectName("edit_dialog")
        edit_dialog.resize(1003, 767)
        self.buttonBox = QtWidgets.QDialogButtonBox(edit_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(770, 730, 192, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_9 = QtWidgets.QLabel(edit_dialog)
        self.label_9.setGeometry(QtCore.QRect(230, 20, 441, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.splitter_2 = QtWidgets.QSplitter(edit_dialog)
        self.splitter_2.setGeometry(QtCore.QRect(190, 140, 241, 551))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.splitter = QtWidgets.QSplitter(edit_dialog)
        self.splitter.setGeometry(QtCore.QRect(441, 141, 431, 551))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.page_count_spinbox = QtWidgets.QSpinBox(self.splitter)
        self.page_count_spinbox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page_count_spinbox.setFont(font)
        self.page_count_spinbox.setObjectName("page_count_spinbox")
        self.year_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.year_input.setFont(font)
        self.year_input.setObjectName("year_input")
        self.description_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_input.setFont(font)
        self.description_input.setObjectName("description_input")
        self.isbn_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.isbn_input.setFont(font)
        self.isbn_input.setObjectName("isbn_input")
        self.id_spinbox = QtWidgets.QSpinBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_spinbox.setFont(font)
        self.id_spinbox.setObjectName("id_spinbox")
        self.no = QtWidgets.QRadioButton(self.splitter)
        self.no.setObjectName("no")
        self.yes = QtWidgets.QRadioButton(self.splitter)
        self.yes.setObjectName("yes")
        self.author_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.author_input.setFont(font)
        self.author_input.setObjectName("author_input")
        self.name_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")

        self.retranslateUi(edit_dialog)
        self.buttonBox.accepted.connect(edit_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(edit_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(edit_dialog)

    def retranslateUi(self, edit_dialog):
        _translate = QtCore.QCoreApplication.translate
        edit_dialog.setWindowTitle(_translate("edit_dialog", "Dialog"))
        self.label_9.setText(_translate("edit_dialog", "Edit Book"))
        self.label.setText(_translate("edit_dialog", "ID"))
        self.label_2.setText(_translate("edit_dialog", "Name"))
        self.label_3.setText(_translate("edit_dialog", "Description"))
        self.label_4.setText(_translate("edit_dialog", "ISBN"))
        self.label_5.setText(_translate("edit_dialog", "Page Count"))
        self.label_7.setText(_translate("edit_dialog", "Issued"))
        self.label_8.setText(_translate("edit_dialog", "Author"))
        self.label_6.setText(_translate("edit_dialog", "Year"))
        self.description_input.setText(_translate("edit_dialog", "fff"))
        self.no.setText(_translate("edit_dialog", "No"))
        self.yes.setText(_translate("edit_dialog", "Yes"))