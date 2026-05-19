import time
from logger import logger
from copier import directory_walk

from watchdog.events import DirModifiedEvent, FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer

# in MacOS, The .DS_Store file is recording any changes of inside the directory
# If the content of the file changes, only FileModifiedEvent is triggered. 
# If a new file is created, a DirmodifiedEvent is triggered.
# When openning a file in vscode (maybe other editors, too), a FileModifiedEvent is triggered
# When pasting a file in the montiered directory (from copy or move), a DirModifiedEvent will be triggered 
# 
# One idea, maybe this sync tool don't need to do real time monitor, I think check in every 15 minutes to see if any file has changed. 
class DirModifiedHandler(FileSystemEventHandler):
    # overide the init method
    def __init__(self, source_dir: str, target_dir: str):
        super().__init__()
        self.source = source_dir
        self.target = target_dir

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if type(event) == DirModifiedEvent:
            print(f"Directory changed, event: {event}")
            logger.info(f"Directory changed, event: {event}")
            print("Start copying from source to target")
            directory_walk(self.source, self.target)
            print("End copying")
        else:
            print(f'file change event: {event}')
            if not event.src_path.endswith("/.DS_Store"):
                logger.info(f"file changed, event: {event}")
                print("Start copying from source to target")
                directory_walk(self.source, self.target)
                print("End copying")

if __name__ == "__main__":
    PATH = '/Users/albsun/Documents/testing/from/'
    event_handler = DirModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler, path=PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(600)
    finally:
        observer.stop()
        observer.start()