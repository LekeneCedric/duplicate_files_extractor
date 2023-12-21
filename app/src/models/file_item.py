import sys

sys.path.append('../../app/src/enums')

from files_type import file_type

class file_item:
    def __init__(
        self,
        name: str,
        type: file_type,
        file_path: str,
        childs: list = [],
        number_duplicates: int = 0,
        duplicates: dict = {}
        ):
        self.name = name
        self.type = type
        self.file_path = file_path
        self.childs = childs
        self.number_duplicates = number_duplicates
        self.duplicates = duplicates

    def add_child(self, child: 'file_item'):
        self.childs.append(child)

    def get_childs(self) -> 'file_item':
        return self.childs

    def extract_duplicates(self):
        self.number_duplicates = 0
        self.duplicates = {}
