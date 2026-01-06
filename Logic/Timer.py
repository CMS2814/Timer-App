# from datetime import datetime
import time
import keyboard

## -------------------------## Stopwatch functions ## -------------------------##


class Stopwatch:
    def __init__(self):
        self._time = 0
        self.isGoing = True
        self.stopWatch = ""
        self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))

    def start(self):
        self.isGoing = True
        self.update()

    def stop(self):
        self.isGoing = False

    def update(self):
        while self.isGoing:
            time.sleep(1)
            self._time += 1
            self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))
            print(self.text)

            if keyboard.is_pressed("s"):
                self.stop()
                print("Stopwatch stopped")


stopwatch = Stopwatch()


def printit():
    print("print")


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    stopwatch.start()
    stopwatch.stop()
