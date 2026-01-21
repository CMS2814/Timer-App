import time
from datetime import datetime, timedelta


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

    def format_td(seconds, digits=3):
        isec, fsec = divmod(round(seconds * 10**digits), 10**digits)
        return f"{timedelta(seconds=isec)}.{fsec:0{digits}.0f}"

    def updateTime(self):
        if not self.startTime:
            return
        if not self.isPaused:
            currentTime = time.monotonic()
            elapsedTime = currentTime - self.startTime
            # elapsedTimeStr = time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
            elapsedTimeTD = timedelta(seconds=elapsedTime)
            elapsedTimeStr = str(elapsedTimeTD)[:-4]
            print("Elapse time:", elapsedTimeStr)
            return


if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.start()
    while not stopwatch.isPaused:
        time.sleep(0.10)
        stopwatch.updateTime()
