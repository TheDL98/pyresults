from PySide6.QtWidgets import QMainWindow, QTabWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("PyResults")
        tabs = QTabWidget()
        
        button = QPushButton("helltto")
        tabs.addTab(button, "&Input")
        tabs.addTab(button,"&Search")
#        tabs.addTab("&Results")
#        tabs.addTab("&Export")
#        tabs.addTab("Se&ttings")
        
        self.setCentralWidget(tabs)