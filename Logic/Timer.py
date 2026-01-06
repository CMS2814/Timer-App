# from datetime import datetime
import time
import keyboard

## -------------------------## Stopwatch functions ## -------------------------##


class Stopwatch:
    def __init__(self):
        self._time = 1
        self.isGoing = True
        self.stopWatch = ""
        self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))

    def start(self):
        self.isGoing = True
        self.update()

    def stop(self):
        self.isGoing = False

    def resume(self):
        self.isGoing = True

    def update(self):
        while self.isGoing:
            if self._time > 0:
                print(self.text)
                time.sleep(1)
                self._time += 1
                self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))

            if keyboard.is_pressed("s"):
                self.stop()
                print("Stopwatch stopped")

            if keyboard.is_pressed("r"):
                self.reset()
                print("Stopwatch reset")

    def reset(self):
        self._time = 0
        self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))


stopwatch = Stopwatch()


def printit():
    print("print")


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    stopwatch.start()
