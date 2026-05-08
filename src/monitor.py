import time
from logger import logger

from watchdog.events import DirModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer

PATH = '.'

class DirModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event: DirModifiedEvent) -> None:
        print(f"Directory changed, event: {event}")
        logger.info(f"Directory changed, event: {event}")

event_handler = DirModifiedEvent()
observer = Observer()
observer.schedule(event_handler=event_handler, path=PATH, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.start()