# from datetime import datetime
import time
from datetime import datetime, timedelta
import keyboard


## -------------------------## Stopwatch functions ## -------------------------##
class Stopwatch:  # To be remade
    def __init__(self):
        self.isPaused = True
        self.isStarted = False
        self.startTime = None
        self.time = 0

    def start(self):
        self.isPaused = False
        self.isStarted = True
        self.startTime = time.monotonic()
        print("Stopwatch started")

    def pause(self):
        if not self.isPaused:
            self.isPaused = True
            print("Stopwatch paused")

    def resume(self):
        if self.isPaused:
            self.isPaused = False
            print("Stopwatch resumed")

    def reset(self):
        if self.isStarted:
            self.isStarted = False
            self.startTime = None
            self.isPaused = True
            print("Stopwatch reset")

    def updateTime(self):
        if not self.startTime:
            return
        if not self.isPaused:
            currentTime = time.monotonic()
            elapsedTime = currentTime - self.startTime
            print("Elapse time:", elapsedTime)
            return str(round(elapsedTime, 2))


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##


## -------------------------## Timer functions ## -------------------------##\
class Timer:
    def __init__(self, timeDuration: int = None):
        self.isPaused = True
        self.isStarted = False
        self.startTime = None
        self.duration = timeDuration

    def start(self):
        if not self.duration:
            return
        self.isPaused = False
        self.isStarted = True
        self.startTime = time.monotonic()
        print("Timer started")
        print(self.duration)

    def pause(self):
        if not self.isPaused:
            self.isPaused = True
            print("Timer paused")

    def resume(self):
        if self.isPaused:
            self.isPaused = False
            print("Timer resumed")

    def reset(self):
        if self.isStarted:
            self.isStarted = False
            self.startTime = None
            self.isPaused = True
            print("Timer reset")

    def updateTime(self):
        if not self.startTime or self.duration is None:
            return
        if not self.isPaused:
            currentTime = time.monotonic()
            elapsedTime = currentTime - self.startTime
            remainingTime = max(0, self.duration - elapsedTime)
            print("Remaining time:", remainingTime)
            return str(round(remainingTime, 2))


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Timer functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.start()
    while not stopwatch.isPaused:
        time.sleep(0.10)
        stopwatch.updateTime()
