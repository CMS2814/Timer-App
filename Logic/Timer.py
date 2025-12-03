# Timer.py
from datetime import datetime
from PyQt6.QtCore import QTimer


## -------------------------## Timer functions ## -------------------------##
def start_timer():
    current_time = datetime.now()
    print(current_time)


def stop_timer():
    pass


def reset_timer():
    pass


def pause_timer():
    pass


def resume_timer():
    pass


def get_time():
    pass


def timer_tick(time):
    print(time)
    time -= 1


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Timer functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##

if __name__ == "__main__":
    time = 60

    Timer = QTimer()
    Timer.timeout.connect(timer_tick(time))
    Timer.start(1000)  # Timer will tick every 1000 milliseconds (1 second)
