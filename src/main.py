# import copier
import monitor
import time

TESTING_SRC = "/Users/albsun/Documents/testing/from/"
TESTING_DEST = "/Users/albsun/Documents/testing/to/"

if __name__ == "__main__":
    # print("testing directory copy based on Path.walk")
    # copier.directory_walk(TESTING_SRC, TESTING_DEST)
    # print("===done===")
    event_handler = monitor.DirModifiedHandler(TESTING_SRC, TESTING_DEST)
    observer = monitor.Observer()
    observer.schedule(event_handler, path=TESTING_SRC, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(600)
    finally:
        observer.stop()
        observer.start()
