from PySide6.QtWidgets import QMainWindow, QTabWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
import sqlite3


class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("PyResults")

        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        widget = QWidget()

        label = QLabel("Enter Text: ")
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.get)

        button = QPushButton("Get data")
        button.clicked.connect(self.get)
        self.result_label = QLabel("placeholder")

        hlayout.addWidget(label)
        hlayout.addWidget(self.line_edit)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(button)
        vlayout.addWidget(self.result_label)
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

        # tabs = QTabWidget()
        
        # btn_insert = QPushButton("helltto")
        # tabs.addTab(btn_insert, "&Input")
        # tabs.addTab(button,"&Search")
        # tabs.addTab("&Results")
        # tabs.addTab("&Export")
        # tabs.addTab("Se&ttings")
        
        # self.setCentralWidget(tabs)

    def get(self):
        self.result_label.setText(self.line_edit.text())
        with sqlite3.connect("results.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO MainCategories (MainCategoryName) VALUES (?);", (self.line_edit.text(),))
            