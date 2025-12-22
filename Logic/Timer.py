from datetime import datetime

## -------------------------## Stopwatch functions ## -------------------------##


def start_stopwatch():
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M:%S:%f")[:-3]
    print(formatted_time)


def stop_stopwatch():
    stop = input("Type s to stop: ").lower()
    return stop


def reset_stopwatch():
    pass


def pause_stopwatch():
    pass


def resume_stopwatch():
    pass


## ^^^^^^^^^^^^^^^^^^^^^^^^^## Stopwatch functions ## ^^^^^^^^^^^^^^^^^^^^^^^^^##
if __name__ == "__main__":
    pass
