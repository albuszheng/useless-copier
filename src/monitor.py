import time
from logger import logger

from watchdog.events import DirModifiedEvent, FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer

PATH = '/home/albsun/Documents/testing/from/'

class DirModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        print(f"Directory changed, event: {event}")
        logger.info(f"Directory changed, event: {event}")

event_handler = DirModifiedHandler()
observer = Observer()
observer.schedule(event_handler, path=PATH, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.start()