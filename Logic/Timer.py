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
    def __init__(self):
        self.time = 0
        self.goal = 0
        self.isGoing = True
        self.isReset = True
        self.stopWatch = ""
        self.text = time.strftime("%H:%M:%S", time.gmtime(self.time))

    def start(self):
        if self.isReset:
            while True:
                try:
                    goalTime = int(input("Enter goal time in seconds:"))
                    self.goal = goalTime
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer value.")
            self.isReset = False
            self.isGoing = True
            print("Timer started")
            self.update()

    def stop(self):
        if self.isGoing:
            self.isGoing = False
            print("Timer stopped")
            time.sleep(0.1)

    def resume(self):
        if not self.isGoing:
            self.isGoing = True
            print("Stopwatch resumed")
            time.sleep(0.1)

    def reset(self):
        if not self.isGoing:
            self.isReset = True
            self.time = 0
            self.goal = 0
        print("Timer reset")

    def update(self):
        curTime = datetime.now()
        while self.goal > 0:
            if self.isGoing:
                TargetTime = datetime.now() - curTime
                if TargetTime >= timedelta(seconds=self.time):
                    timetext = timedelta(seconds=self.goal)
                    print(timetext)
                    self.time += 1
                    self.goal -= 1

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
        print("Timer finished!")


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Timer functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    stopwatch = Stopwatch()
    timer = Timer()
    timer.start()
