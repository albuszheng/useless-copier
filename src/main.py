import copier

TESTING_SRC = "/home/albsun/Documents/testing/from/"
TESTING_DEST = "/home/albsun/Documents/testing/to/"

if __name__ == "__main__":
    print("testing directory copy based on Path.walk")
    copier.directory_walk(TESTING_SRC, TESTING_DEST)
    print("===done===")
