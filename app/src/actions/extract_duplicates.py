import sys
sys.path.append('../../app/src/models')
sys.path.append('../../app/src/enums')

from duplicates_checker import check_duplicates_files
from hashfile import get_hash_file
from file_item import file_item
from files_type import file_type
from os import system

def filter_files_in_root(file_item: file_item):
    return file_item.type == file_type.FILE

def filter_folder_in_root(file_item: file_item):
    return file_item.type == file_type.DIR

class duplicates_extracter:
    def __init__(self, duplicates: dict = {}):
        self.duplicates = duplicates

    def extract_duplicates(self, root: file_item):
        root_files = filter(filter_files_in_root, root.childs)
        root_folders = filter(filter_folder_in_root, root.childs)
        for file in root_files:
            file_path = file.file_path
            hash = get_hash_file(file_path)

            if hash not in self.duplicates:
                self.duplicates[hash] = [file_path]
            else:
                self.duplicates[hash].append(file_path)

        for folder in root_folders:
            self.extract_duplicates(folder)

    def return_duplicates(self) -> dict:
        return self.duplicates

def extract_duplicates(root: file_item):

    extracter = duplicates_extracter({})
    extracter.extract_duplicates(root)

    return extracter.return_duplicates()


