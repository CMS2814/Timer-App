# from datetime import datetime
import time
from threading import Timer

## -------------------------## Stopwatch functions ## -------------------------##


def start_stopwatch(text, _time=0):
    _time += 1
    text = time.strftime("%H:%M:%S", time.gmtime(_time))
    return text, _time


def stop_stopwatch():
    stop = input("Type s to stop: ").lower()
    return stop


def reset_stopwatch():
    pass


def pause_stopwatch():
    pass


def resume_stopwatch():
    pass


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    _time = 0
    isGoing = True
    stopWatch = ""
    stopWatch, _time = start_stopwatch(stopWatch, _time)
    while isGoing:
        Timer(
            3,
        )
