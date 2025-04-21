from PyQt6.QtCore import QTimer


class TimerLogic:
    def __init__(self, ui_update_back):
        
        self.modes = [
            {"name": "25/5", "worktime": 25*60, "breaktime": 5*60},
            {"name": "30/10", "worktime": 30*60, "breaktime": 10*60},
            {"name": "45/15", "worktime": 45*60, "breaktime": 15*60}
        ]
        self.current_mode = 0
        self.is_work_phase = True
        self.time_left = self.modes[self.current_mode]["worktime"]
        self.is_running = False
        self.ui_update = ui_update_back  
        
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_timer)
        self.timer.setInterval(1000)
        
        self._update_ui()

    def _update_ui(self):

        time_str = f"{self.time_left // 60:02d}:{self.time_left % 60:02d}"
        mode_str = f"{self.modes[self.current_mode]['name']} | {'Работа' if self.is_work_phase else 'Отдых'}"
        self.ui_update(time_str, mode_str, self.is_running)

    def _update_timer(self):

        self.time_left -= 1
        
        if self.time_left <= 0:
            self._switch_phase()
        
        self._update_ui()

    def _switch_phase(self):

        self.is_work_phase = not self.is_work_phase
        
        if self.is_work_phase:
            self.current_mode = (self.current_mode + 1) % len(self.modes)
            self.time_left = self.modes[self.current_mode]["worktime"]
        else:
            self.time_left = self.modes[self.current_mode]["breaktime"]
        

    def toggle_timer(self):
        """Запуск/пауза таймера"""
        if not self.is_running:
            self.timer.start()
            self.is_running = True
        else:
            self.timer.stop()
            self.is_running = False
        self._update_ui()

    def reset_timer(self):
        """Сброс таймера"""
        self.timer.stop()
        self.is_running = False
        self.is_work_phase = True
        self.time_left = self.modes[self.current_mode]["worktime"]
        self._update_ui()

    def change_mode(self, mode_index):
        if 0 <= mode_index < len(self.modes):
            self.current_mode = mode_index
            self.reset_timer()

