import time

from watchdog.events import DirModifiedEvent, FileModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer

from copier import directory_walk
from logger import logger


# in MacOS, The .DS_Store file is recording any changes of inside the directory
# If the content of the file changes, only FileModifiedEvent is triggered.
# If a new file is created, a DirmodifiedEvent is triggered.
# When openning a file in vscode (maybe other editors, too), a FileModifiedEvent is triggered
# When pasting a file in the montiered directory (from copy or move), a DirModifiedEvent will be triggered
#
# One idea, maybe this sync tool don't need to do real time monitor, I think check in every 15 minutes to see if any file has changed.
#
# To prevent the cascading loop of changes being synced between 2 locations,
# there are two strategies I'm considering:
# 1. Use the timestamp of changes, any changes within a time threshold (let's say 1 minute) will not trigger a file copy event
#    The comparison is between the timestamp of file modified in meta data and the system time.
#    It's probably the simplest solution, however, it may cause a problem if one file is changed in rapid fashion (3 legit file modified events is triggered in 1 minute), 
#    any changes other than the first one will not be synced. 
#    And the unsynced changes may never be synced if no further file modified signal is triggered.
# 2. Use the content changes (checksum) to check if the content of the file is changed. 
#    I can use the hashlib module in Python to calculate the checksum of the two file to determine if the content is actually changed.
#    This will naturally break the loop, and can be adapted to fit non real time monitor.
#    The computational (CPU usage) is unknown. 
class DirModifiedHandler(FileSystemEventHandler):
    # overide the init method
    def __init__(self, source_dir: str, target_dir: str):
        super().__init__()
        self.source = source_dir
        self.target = target_dir

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if isinstance(event, DirModifiedEvent):
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
