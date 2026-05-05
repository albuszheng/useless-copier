# import sys
import logging
import os
from pathlib import Path
from shutil import copy2

logging.basicConfig(
    filename="copier.log", format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


def copy_file(source: str, target: str) -> None:
    """
    Copies a file from source to destination.
    If target already exists, it will be overwritten without warning.

    The destination directory need to be created first before copying
    files into it. The function will not create the necessary directory path

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


def directory_walk(source: str, target: str) -> None:
    """
    Using Path.walk to copy the file and the directory structure of the
    source directory to the target directory

    TODO: error handling with the Path.walk
    TODO: Further testing on a more complex directory structure

    :param source: Path to the source directory
    :param target: Path to the target directory
    """
    if source[-1] == "/":  # removing the trailing '/' to match the format of Path
        source = source[:-1]
    path_src = Path(source)
    if path_src.is_dir():
        for root, dirs, files in path_src.walk(on_error=None):
            logger.debug(f"root value: {root}, source value: {source}")
            sub_directory = str(root).replace(source, "")
            for file in files:
                if os.path.exists(target + f"{sub_directory}/{file}"):
                    copy_file(str(root / file), target + f"{sub_directory}/{file}")
                else:
                    target_path = Path(target + f"{sub_directory}/{file}")
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    copy_file(str(root / file), str(target_path))
    else:
        # TODO: if the source is not a directory, should raise an error
        pass
