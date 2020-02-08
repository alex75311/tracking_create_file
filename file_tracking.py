from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path.split('\\')[-1])


if __name__ == '__main__':
    path = os.getcwd()
    observer = Observer()
    observer.schedule(Handler(), path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
