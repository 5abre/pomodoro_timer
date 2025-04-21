import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Таймер")
        self.setFixedSize(250, 250)  
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    

        layout = QVBoxLayout()

        layout.addStretch(1)


        self.start_button = QPushButton("Старт", self)
        self.stop_button = QPushButton("Стоп", self)
        self.stop_button.setEnabled(False)
        self.timer_label = QLabel('00:00', self)
        layout.addWidget(self.timer_label, alignment=Qt.AlignmentFlag.AlignCenter)



        layout.addWidget (self.timer_label)
        layout.addWidget(self.start_button)
        layout.setSpacing(10) 
        layout.addWidget(self.stop_button)
        

        layout.addStretch(5)


        central_widget.setLayout(layout)

        self.start_button.clicked.connect(self.start_action)
        self.stop_button.clicked.connect(self.stop_action)

    def start_action(self):
        print("Процесс запущен")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_action(self):
        print("Процесс остановлен")
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
