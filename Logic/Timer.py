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
        if self.isGoing:
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
                _Time = datetime.now() - curTime
                if _Time >= timedelta(milliseconds=self._time):
                    self._time += 10
                    timetext = timedelta(milliseconds=self._time)
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
            self._time = 0
            self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))
            print("Stopwatch reset")
            time.sleep(0.1)


stopwatch = Stopwatch()

## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    stopwatch.start()
