from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QApplication
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShareMe")
        self.resize(800, 701)
        self.root = QVBoxLayout()
        self.root.setContentsMargins(0,0,0,0)
        self.setLayout(self.root)
        self.webView = QtWebEngineWidgets.QWebEngineView()
        self.webView.load(QUrl("file:///home/shivanshu/Documents/Projects/shareme/res/main.html"))
        #self.webView.load(QUrl("http://www.google.com"))
        self.webView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.root.addWidget(self.webView)
    
    def navigate_to_url(self, site): 
        q = QUrl(sit) 
        if q.scheme() == "": 
            q.setScheme("http") 
        self.tabs.currentWidget().setUrl(q) 
  

def main():
    import sys
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())

main()