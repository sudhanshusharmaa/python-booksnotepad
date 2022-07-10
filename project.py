from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from delete_dialog import Ui_delete_dialog as Ui_Delete_Dialog
from edit_dialog import Ui_edit_dialog as Ui_Edit_Dialog
from add_book_dialog import Ui_Dialog as Ui_Add_Dialog
from main_books_window import Ui_MainWindow
import my_functions as lib
from stylesheetss import main_style_sheet

# Main Window

class Delete_Dialog (QDialog):
    def __init__(self,parent=None):
        super(Delete_Dialog,self).__init__(parent)
        self.ui = Ui_Delete_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class Edit_Dialog (QDialog):
    def __init__(self,parent=None):
        super(Edit_Dialog,self).__init__(parent)
        self.ui = Ui_Edit_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

class Add_Dialog (QDialog):
    def __init__(self,parent=None):
        super(Add_Dialog,self).__init__(parent)
        self.ui = Ui_Add_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.new_book_button.pressed.connect(self.show_add_dialog)
        self.load_issued_table()
        self.load_unissued_table()
        self.load_all_books_table()
        self.edit_issued.clicked.connect(lambda: self.edit_book(self.Issued_books_table))
        self.delete_issued.pressed.connect(
            lambda: self.delete_book(self.Issued_books_table)
        )
        self.refresh_issued.clicked.connect(self.load_issued_table)
        self.edit_unissued.clicked.connect(lambda: self.edit_book(self.Unissued_books_table))
        self.delete_unissued.pressed.connect(
            lambda: self.delete_book(self.Unissued_books_table)
        )
        self.refresh_btn.clicked.connect(self.load_all_books_table)

# comments

        self.refresh_issued.clicked.connect(self.load_issued_table)

# Search button 
        self.search_btn.clicked.connect(self.search_book)
        self.setStyleSheet(main_style_sheet)


    def save_existing_book(self,ui):
        book = {
            'id': int(ui.page_count_spinbox.text()),
            'name': ui.year_input.text(),
            'description': ui.description_input.text(),
            'isbn': ui.isbn_input.text(),
            'page_count': int(ui.id_spinbox.text()),
            'issued': ui.yes.isChecked(),
            'author': ui.author_input.text(),
            'year': int(ui.name_input.text())
        }
        lib.update_book(book)

    def edit_book(self,table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row,0).text())
            book = lib.find_books(book_id)
            # Creating the dialog
            dialog = Edit_Dialog()
            dialog.ui.page_count_spinbox.setValue(int(book.id))
            dialog.ui.year_input.setText(book.name)
            dialog.ui.description_input.setText(book.description)
            dialog.ui.isbn_input.setText(book.isbn)
            dialog.ui.id_spinbox.setValue(int(book.page_count))
            dialog.ui.yes.setChecked(book.issued)
            if book.issued == False:
                dialog.ui.no.setChecked(True)
            dialog.ui.author_input.setText(book.author)
            dialog.ui.name_input.setValue(int(book.year))

            dialog.ui.buttonBox.accepted.connect(
                lambda: self.save_existing_book(dialog.ui))
            dialog.exec()
            self.load_issued_table()
            self.load_unissued_table()

    def save_new_book(self,ui):
        # print(ui.page_count_spinbox.text())
 # creating a dictionary to store all the values
        new_book = {
            'id': int(ui.page_count_spinbox.text()),
            'name': ui.year_input.text(), 
            'description': ui.description_input.text(),
            'isbn': ui.isbn_input.text(), 
            'page_count': int(ui.id_spinbox.text()),
            'issued': ui.yes.isChecked(),
            'author': ui.author_input.text(),
            'year': int(ui.name_input.text())   }

        for attr in new_book:
            if new_book[attr] == None or str(new_book[attr]) == "":
                return False
        lib.add_book(new_book)
        self.load_issued_table()
        self.load_unissued_table()

    def search_book(self):
        if self.search_input.text() != "":
            book = lib.find_books(int(self.search_input.text()))
            if book != None:
                self.search_table.setRowCount(1)
                book_dict = book.to_dict()
                for book_index, attr in enumerate(book_dict):
                    self.search_table.setItem(
                        0,book_index,QTableWidgetItem(str(book_dict[str(attr)])))
                    self.search_table.item(0, book_index).setFlags(
                        Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_issued_table(self):
        books = lib.get_issued_books()
        self.Issued_books_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.Issued_books_table.setItem(
                    index,book_index,QTableWidgetItem(str(book[str(attr)])))
                self.Issued_books_table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def delete_book(self,table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            dialog = Delete_Dialog()
            dialog.ui.buttonBox.accepted.connect(
                lambda: lib.delete_book(book_id)
            )
            dialog.exec()
            self.load_issued_table()
            self.load_unissued_table()


    def load_unissued_table(self):
        books = lib.get_unissued_books()
        self.Unissued_books_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.Unissued_books_table.setItem(
                    index,book_index,QTableWidgetItem(str(book[str(attr)])))
                self.Unissued_books_table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    

    def load_all_books_table(self):
        books = lib.load_books()
        self.all_books_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.all_books_table.setItem(
                    index,book_index,QTableWidgetItem(str(book[str(attr)])))
                self.all_books_table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)


    def show_add_dialog(self):
        input_dlg = Add_Dialog()
        input_dlg.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dlg.ui))
        input_dlg.exec()





    

app = QApplication([])
window = MainWindow()
window.show()
app.exec()


