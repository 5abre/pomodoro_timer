
from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from app.services.pomodoro_logic import TimerLogic
from app.ui.window import MainWindow

class PomodoroApp(MainWindow):
    def __init__(self):
        super().__init__()
        
        central_widget = self.centralWidget()
        layout = central_widget.layout()
        
        self.status_label = QLabel('Режим: 25/5 | Работа')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.insertWidget(1, self.status_label)
        
        self.pomodoro = TimerLogic(self.update_ui)
        
        self.start_button.clicked.disconnect()
        self.stop_button.clicked.disconnect()
        self.start_button.clicked.connect(self.pomodoro.toggle_timer)
        self.stop_button.clicked.connect(self.pomodoro.reset_timer)
        
        self.pomodoro.reset_timer()
    
    def update_ui(self, time_str, mode_str, is_running):
        self.timer_label.setText(time_str)
        self.status_label.setText(f"Режим: {mode_str}")
        self.start_button.setText("Пауза" if is_running else "Старт")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(is_running)