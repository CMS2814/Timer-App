# from datetime import datetime
import time
from datetime import datetime, timedelta
import keyboard


## -------------------------## Stopwatch functions ## -------------------------##
class Stopwatch:  # To be remade
    def __init__(self):
        self.time = 0
        self.isGoing = True
        self.isReset = True
        self.stopWatch = ""

    def start(self):
        if self.isReset:
            self.isReset = False
            print(self.isReset)
            self.isGoing = True
            self.update()
            print("Stopwatch started")

    def stop(self):
        self.isGoing = False
        print("Stopwatch stopped")
        time.sleep(0.1)

    def resume(self):
        if not self.isGoing:
            self.isGoing = True
            print("Stopwatch resumed")
            time.sleep(0.1)

    def update(self):
        curTime = datetime.now()
        while True:
            if self.isGoing:
                TargetTime = datetime.now() - curTime
                if TargetTime >= timedelta(milliseconds=self.time):
                    self.time += 10
                    timetext = timedelta(milliseconds=self.time)
                    print(timetext)

            if keyboard.is_pressed("space"):
                self.stop()
            elif keyboard.is_pressed("r"):
                self.reset()
            elif keyboard.is_pressed("space"):
                self.resume()
            elif keyboard.is_pressed("s"):
                self.start()
            elif keyboard.is_pressed("q"):
                print("Quitting program")
                break

    def reset(self):
        if not self.isGoing:
            self.isReset = True
            self.time = 0
            print("Stopwatch reset")
            time.sleep(0.1)


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
    timer = time.monotonic()
    print(timer)
