import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.presentation.Mainkal import PomodoroApp
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.setWindowTitle("Pomodoro Timer")
    window.setFixedSize(300, 250)
    window.show()
    sys.exit(app.exec())
