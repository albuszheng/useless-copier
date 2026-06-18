# import copier
import monitor
import time

TESTING_SRC = "/Users/albsun/Documents/testing/from/"
TESTING_DEST = "/Users/albsun/Documents/testing/to/"

if __name__ == "__main__":
    # print("testing directory copy based on Path.walk")
    # copier.directory_walk(TESTING_SRC, TESTING_DEST)
    # print("===done===")
    event_handler_src = monitor.DirModifiedHandler(TESTING_SRC, TESTING_DEST)
    event_handler_tar = monitor.DirModifiedHandler(TESTING_DEST, TESTING_SRC)
    observer = monitor.Observer()
    observer.schedule(event_handler_src, path=TESTING_SRC, recursive=True)
    observer.schedule(event_handler_src, path=TESTING_DEST, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join()
    finally:
        observer.stop()
        observer.start()
