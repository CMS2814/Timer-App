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
        self._time = 1
        self.update()

    def stop(self):
        self.isGoing = False

    def resume(self):
        self.isGoing = True

    def update(self):
        while self._time > 0:
            if self.isGoing:
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

            if keyboard.is_pressed("c"):
                self.resume()
                print("Stopwatch resumed")

    def reset(self):
        if not self.isGoing:
            self._time = 0
            self.text = time.strftime("%H:%M:%S", time.gmtime(self._time))


stopwatch = Stopwatch()


def printit():
    print("print")


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    stopwatch.start()
