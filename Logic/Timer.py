# from datetime import datetime
import time
from datetime import datetime, timedelta
import keyboard


## -------------------------## Stopwatch functions ## -------------------------##
class Stopwatch:
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
    def __init__(self, timeDuration=None):
        self.duration = timeDuration or 0
        self.startTime = None

    def start(self):
        self.startTime = time.monotonic()

    def pause(self):
        pass

    def resume(self):
        pass

    def reset(self):
        pass

    def updateTime(self):
        if not self.startTime:
            return
        currentTime = time.monotonic()
        elapsedTime = currentTime - self.startTime
        remainingTime = self.duration - elapsedTime
        return remainingTime


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Timer functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    timer = time.monotonic()
    print(timer)
