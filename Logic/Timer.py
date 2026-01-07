# from datetime import datetime
import time
from datetime import datetime, timedelta
import keyboard


## -------------------------## Stopwatch functions ## -------------------------##


class Stopwatch:
    def __init__(self):
        self._time = 0
        self.isGoing = True
        self.isReset = True
        self.stopWatch = ""
        self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))

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

    def resume(self):
        self.isGoing = True
        print("Stopwatch resumed")

    def update(self):
        while True:
            if self.isGoing:
                print(self.text)
                time.sleep(1)
                self._time += 1
                self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))

            if keyboard.is_pressed(
                "p"
            ):  # for some reason i have to hold s for it to work or spam it
                self.stop()

            if keyboard.is_pressed("r"):
                self.reset()

            if keyboard.is_pressed("c"):
                self.resume()

            if keyboard.is_pressed("s"):
                self.start()

            if keyboard.is_pressed("q"):
                print("Quitting program")
                break

    def reset(self):
        if not self.isGoing:
            self.isReset = True
            self._time = 0
            self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))
            print("Stopwatch reset")


stopwatch = Stopwatch()

## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    i = 0
    curTime = datetime.now()
    while True:
        _Time = datetime.now() - curTime
        if _Time >= timedelta(seconds=i):
            i += 1
            timetext = timedelta(seconds=i)
            print(timetext)
