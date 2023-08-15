import os
import logging
from collections import namedtuple
import sys

# Настройка логирования
logging.basicConfig(filename='log.txt', level=logging.INFO)

# Определение namedtuple
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def process_directory(dir_path):
    for root, directories, files in os.walk(dir_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            parent_directory = os.path.basename(root)
            is_directory = False
            file_info = FileInfo(file_name, file_extension, is_directory, parent_directory)
            logging.info(file_info)

        for directory in directories:
            parent_directory = os.path.basename(root)
            is_directory = True
            file_info = FileInfo(dir, '', is_directory, parent_directory)
            logging.info(file_info)


if __name__ == "__main__":
    p_name = sys.argv[1]
    process_directory(p_name)
