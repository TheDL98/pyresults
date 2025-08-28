import sqlite3
import xlsxwriter
from db_init import db_init
from PySide6.QtWidgets import QApplication
import sys
import main_window


db_init()

app = QApplication(sys.argv)

a = main_window.MainWindow()
a.show()

app.exec()