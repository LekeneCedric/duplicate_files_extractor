import sys
from os import path

sys.path.append('models/')
sys.path.append('enums/')
sys.path.append('actions/')

from file_item import file_item
from files_type import file_type
from files_operations import list_dir, load_file, read_root


ROOT_PATH = '/home/code237/Videos/MANGA'
if __name__ == '__main__':

  files = list_dir(ROOT_PATH)

  root = file_item('root', file_type.DIR, ROOT_PATH,[])

  for file in files:

      file = path.join(ROOT_PATH, file)
      is_dir = path.isdir(file)
      type = file_type.DIR if is_dir else file_type.FILE

      root.add_child(load_file(file))

  read_root(root)






