# import sys
import os
import logging
from shutil import copy2

logging.basicConfig(filename='copier.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

def copy_file(source: str, target: str) -> None:
    """
    Copies a file from source to destination.
    If target already exists, it will be overwritten without warning.
    
    :param source: Path to the source file.
    :param target: Path to the destination file.
    """
    try:
        if not os.path.isfile(source):
            logger.error(f"Source file does not exist: {source}")
            raise FileNotFoundError(f"Source file does not exist: {source}")

        copy2(source, target)
        logger.info(f"Copied {source} to {target}")
    except PermissionError as e:
        logger.error(f"Permission denied: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise e

def directory_sync(source: str, target: str) -> None:
    "TODO: the function aim to sync the structure and contents of the source directory to the target directory, and perserving the file metadata."
    "TODO: the name of arguments needs consideration, sync function should not have a source and target, since both can be source"
    pass

def modification_check(source: str, target: str) -> str:
    "TODO: function to check which file is more recently modified, returns the path of the more recently modified file."
    pass