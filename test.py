from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,100,100)
        self.show()
        
if __name__ == "__main__":
    print("opened")

    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
