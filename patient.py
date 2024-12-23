# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import mysql_db
import common

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import icon_rc
from constant import *


class UiPatientWindow(QMainWindow):
    def __init__(self, parent=None):
        super(UiPatientWindow, self).__init__(parent)
        self.CNX = None

    def setupUi(self):
        self.setObjectName("PatientWindow")
        self.resize(1200, 1000)
        self.setMinimumSize(QtCore.QSize(1200, 1000))
        self.setMaximumSize(QtCore.QSize(1200, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/fpt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.patient_table = QtWidgets.QTableWidget(self.centralwidget)
        self.patient_table.setGeometry(QtCore.QRect(40, 60, 1021, 551))
        self.patient_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.patient_table.setObjectName("patient_table")
        self.patient_table.setColumnCount(8)
        self.patient_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.patient_table.setHorizontalHeaderItem(7, item)
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(1080, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(1080, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(20, 620, 1161, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_widget.setFont(font)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")
        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.search_box = QtWidgets.QGroupBox(self.search)
        self.search_box.setGeometry(QtCore.QRect(20, 30, 1121, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_box.setFont(font)
        self.search_box.setObjectName("search_box")
        self.search_button = QtWidgets.QPushButton(self.search_box)
        self.search_button.setGeometry(QtCore.QRect(450, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.search_line = QtWidgets.QLineEdit(self.search_box)
        self.search_line.setGeometry(QtCore.QRect(100, 40, 1001, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_line.setFont(font)
        self.search_line.setObjectName("search_line")
        self.search_name = QtWidgets.QLabel(self.search_box)
        self.search_name.setGeometry(QtCore.QRect(10, 45, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.search_name.setFont(font)
        self.search_name.setObjectName("search_name")
        self.tab_widget.addTab(self.search, "")
        self.add_new = QtWidgets.QWidget()
        self.add_new.setObjectName("add_new")
        self.name_line = QtWidgets.QLineEdit(self.add_new)
        self.name_line.setGeometry(QtCore.QRect(170, 20, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_line.setFont(font)
        self.name_line.setObjectName("name_line")
        self.phone_line = QtWidgets.QLineEdit(self.add_new)
        self.phone_line.setGeometry(QtCore.QRect(170, 70, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone_line.setFont(font)
        self.phone_line.setObjectName("phone_line")
        self.address_line = QtWidgets.QLineEdit(self.add_new)
        self.address_line.setGeometry(QtCore.QRect(170, 170, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_line.setFont(font)
        self.address_line.setObjectName("address_line")
        self.add_button = QtWidgets.QPushButton(self.add_new)
        self.add_button.setGeometry(QtCore.QRect(550, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.add_name = QtWidgets.QLabel(self.add_new)
        self.add_name.setGeometry(QtCore.QRect(20, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_name.setFont(font)
        self.add_name.setObjectName("add_name")
        self.add_phone = QtWidgets.QLabel(self.add_new)
        self.add_phone.setGeometry(QtCore.QRect(20, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_phone.setFont(font)
        self.add_phone.setObjectName("add_phone")
        self.add_address = QtWidgets.QLabel(self.add_new)
        self.add_address.setGeometry(QtCore.QRect(20, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_address.setFont(font)
        self.add_address.setObjectName("add_address")
        self.add_hospital_id = QtWidgets.QLabel(self.add_new)
        self.add_hospital_id.setGeometry(QtCore.QRect(20, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_hospital_id.setFont(font)
        self.add_hospital_id.setObjectName("add_hospital_id")
        self.email_line = QtWidgets.QLineEdit(self.add_new)
        self.email_line.setGeometry(QtCore.QRect(170, 120, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_line.setFont(font)
        self.email_line.setObjectName("email_line")
        self.add_email = QtWidgets.QLabel(self.add_new)
        self.add_email.setGeometry(QtCore.QRect(20, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_email.setFont(font)
        self.add_email.setObjectName("add_email")
        self.hospital_id_line = QtWidgets.QLineEdit(self.add_new)
        self.hospital_id_line.setGeometry(QtCore.QRect(170, 220, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hospital_id_line.setFont(font)
        self.hospital_id_line.setObjectName("hospital_id_line")
        self.tab_widget.addTab(self.add_new, "")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action_config = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.retranslateUi()
        # self.patient_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_widget.setCurrentIndex(0)
        self.init_data()
        self.search_button.clicked.connect(self.search_button_click)
        self.add_button.clicked.connect(self.add_button_click)
        self.export_button.clicked.connect(self.export_button_click)
        self.import_button.clicked.connect(self.import_button_click)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PatientWindow", "Patient Manage"))
        self.label.setText(_translate("PatientWindow", "Patients"))
        item = self.patient_table.horizontalHeaderItem(0)
        item.setText(_translate("PatientWindow", "ID"))
        item = self.patient_table.horizontalHeaderItem(1)
        item.setText(_translate("PatientWindow", "Name"))
        item = self.patient_table.horizontalHeaderItem(2)
        item.setText(_translate("PatientWindow", "Phone"))
        item = self.patient_table.horizontalHeaderItem(3)
        item.setText(_translate("PatientWindow", "Email"))
        item = self.patient_table.horizontalHeaderItem(4)
        item.setText(_translate("PatientWindow", "Address"))
        item = self.patient_table.horizontalHeaderItem(5)
        item.setText(_translate("PatientWindow", "Hospital"))
        item = self.patient_table.horizontalHeaderItem(6)
        item.setText(_translate("PatientWindow", "Edit"))
        item = self.patient_table.horizontalHeaderItem(7)
        item.setText(_translate("PatientWindow", "Delete"))
        self.import_button.setText(_translate("PatientWindow", "Import"))
        self.export_button.setText(_translate("PatientWindow", "Export"))
        self.search_box.setTitle(_translate("PatientWindow", "Search patient"))
        self.search_button.setText(_translate("PatientWindow", "Search patient"))
        self.search_name.setText(_translate("PatientWindow", "Name:"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.search), _translate("PatientWindow", "Search"))
        self.add_button.setText(_translate("PatientWindow", "Add"))
        self.add_name.setText(_translate("PatientWindow", "Name:"))
        self.add_phone.setText(_translate("PatientWindow", "Phone:"))
        self.add_address.setText(_translate("PatientWindow", "Address:"))
        self.add_hospital_id.setText(_translate("PatientWindow", "Hospital ID:"))
        self.add_email.setText(_translate("PatientWindow", "Email:"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.add_new), _translate("PatientWindow", "Add New"))

    def show_data_table(self, data):
        self.patient_table.clearContents()
        self.patient_table.setRowCount(0)
        len_data = len(data)
        for i in range(len_data):
            self.patient_table.insertRow(i)
            item = QtWidgets.QTableWidgetItem(str(data[i][0]))
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            self.patient_table.setItem(i, 0, item)
            # self.patient_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i][0])))  # id
            self.patient_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data[i][1])))  # name
            self.patient_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data[i][2])))  # phone
            self.patient_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data[i][3])))  # email
            self.patient_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(data[i][4])))  # address
            self.patient_table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(data[i][5])))  # hospital id

            self.edit_button = QtWidgets.QPushButton(self)
            self.edit_button.clicked.connect(self.edit_button_click)
            self.edit_button.setText("Edit")
            self.patient_table.setCellWidget(i, 6, self.edit_button)

            self.delete_button = QtWidgets.QPushButton(self)
            self.delete_button.clicked.connect(self.delete_button_click)
            self.delete_button.setText("Delete")
            self.patient_table.setCellWidget(i, 7, self.delete_button)

    def connect_database_config(self):
        try:
            config = common.load_json(DATABASE_CONFIG_PATH)
            if config is None:
                QMessageBox.information(self, 'Config Error', 'Config File is not found', QMessageBox.Close)
                self.connect_db_status = False
            print(config)
            connect_success, self.CNX = mysql_db.mysql_connect(config)
            if not connect_success:
                QMessageBox.information(self, 'Database connection Error', self.CNX, QMessageBox.Close)
                self.connect_db_status = False
            self.cursor = self.CNX.cursor()
            use_success = mysql_db.use_database(self.cursor, config['database_name'])
            if not use_success:
                QMessageBox.information(self, 'Database Error', 'Database {} not found'.format(config['database_name']),
                                        QMessageBox.Close)
            self.connect_db_status = True
        except Exception as err:
            print('Something went wrong: {}'.format(err))
            QMessageBox.information(self, 'Error', 'Something went wrong: {}'.format(err), QMessageBox.Close)

    def init_data(self):
        self.connect_database_config()
        if self.connect_db_status is False:
            return
        self.data = mysql_db.search_all_name(self.cursor, 'patient')
        self.show_data_table(self.data)

    def search_button_click(self):
        if self.connect_db_status is False:
            return
        search_name = self.search_line.text()
        self.data = mysql_db.search_all_name(self.cursor, 'patient', search_name)
        self.show_data_table(self.data)

    def delete_button_click(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.patient_table.indexAt(button.pos())
        # if index.isValid():
        #     print(index.row(), index.column())
        table_model = self.patient_table.model()
        id_index = table_model.index(index.row(), 0)
        id = table_model.data(id_index)
        # print(id)
        delete_confirm = QMessageBox.question(self, 'Delete confimation', 'Do you want to delete this row',
                                              QMessageBox.Yes, QMessageBox.Cancel)
        if delete_confirm == QMessageBox.Yes:
            delete_success = mysql_db.delete_row_by_id(self.CNX, self.cursor, 'patient', id)
            if delete_success is False:
                QMessageBox.information(self, 'Delete unsuccessfully', 'Somethings went wrong', QMessageBox.Close)
            self.search_button_click()

    def edit_button_click(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.patient_table.indexAt(button.pos())
        # if index.isValid():
        #     print(index.row(), index.column())
        table_model = self.patient_table.model()
        num_cols = self.patient_table.columnCount()
        update_data = []
        for i in range(num_cols - 2):
            data_index = table_model.index(index.row(), i)
            update_data.append(table_model.data(data_index))
        print(update_data)
        msg = common.check_patient_input(self.cursor, update_data[1], update_data[2], update_data[3],
                                        update_data[4], update_data[5])
        if msg != '':
            QMessageBox.information(self, 'Input data invalid', msg, QMessageBox.Close)
            return
        else:
            edit_confirm = QMessageBox.question(self, 'Edit confimation', 'Do you want to save change this row',
                                                QMessageBox.Yes, QMessageBox.Cancel)
            if edit_confirm == QMessageBox.Yes:
                edit_success = mysql_db.update_patient(self.CNX, self.cursor, update_data[0], update_data[1],
                                                      update_data[2], update_data[3], update_data[4], update_data[5])
                if edit_success is False:
                    QMessageBox.information(self, 'Edit unsuccessfully', 'Somethings went wrong', QMessageBox.Close)
                else:
                    self.search_button_click()

    def add_button_click(self):
        add_name = self.name_line.text().strip()
        add_phone = self.phone_line.text().strip()
        add_email = self.email_line.text().strip()
        add_address = self.address_line.text().strip()
        add_hospital_id = self.hospital_id_line.text().strip()
        # print(mysql_db.select_id(self.cursor, 'hospital'))

        msg = common.check_patient_input(self.cursor, add_name, add_phone, add_email, add_address, add_hospital_id)
        if msg != '':
            QMessageBox.information(self, 'Input data invalid', msg, QMessageBox.Close)
            return
        else:
            insert_success = mysql_db.add_patient(self.CNX, self.cursor, add_name, add_phone,
                                                  add_email, add_address, add_hospital_id)
        if not insert_success:
            QMessageBox.information(self, 'Insert database Error', 'Some input data is too long', QMessageBox.Close)
        else:
            self.name_line.clear()
            self.phone_line.clear()
            self.email_line.clear()
            self.address_line.clear()
            self.hospital_id_line.clear()
            self.search_button_click()

    def import_button_click(self):
        self.import_file = common.open_dialog_file()
        if self.import_file is None:
            return None
        import_data = common.load_excel(self.import_file)
        column_count = self.patient_table.columnCount()
        column_label = []
        for i in range(column_count - 2):
            column_label.append(self.patient_table.horizontalHeaderItem(i).text())
        # print(import_data)
        if column_label != import_data.pop(0):
            QMessageBox.information(self, 'Import data Error',
                                    'Import data from:\n{}\nIs not valid'.format(self.import_file),
                                    QMessageBox.Close)
            return None

        msg = 'Data have been added to database'
        for row in import_data:
            try:
                mysql_db.add_patient(self.CNX, self.cursor, row[1], row[2], row[3], row[4], row[5])
            except:
                msg += '\nWarning:\nSome rows were not added to database'

        QMessageBox.information(self, 'Import successfully', msg, QMessageBox.Close)
        self.init_data()

    def export_button_click(self):
        column_count = self.patient_table.columnCount()
        column_label = []
        for i in range(column_count - 2):
            column_label.append(self.patient_table.horizontalHeaderItem(i).text())
        file_path = common.save_excel('patient', column_label, self.data, EXPORT_PATH)
        QMessageBox.information(self, 'Export successfully', f'Data have been saved to file:\n{file_path}',
                                QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UiPatientWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
