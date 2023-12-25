import subprocess
import sys
from os import path
from pathlib import Path

sys.path.append('../../app/src/models')
sys.path.append('../../app/src/enums')

from file_item import file_item
from files_type import file_type

def format_path(path: str) -> str:

    return path.replace('\ ',' ').replace(' ', '\ ')

def list_dir(path: str) -> list:

   formatted_path = format_path(path)

   command = f'ls {formatted_path}'

   result = subprocess.run(command, shell=True, capture_output=True, text=True)

   files = result.stdout.split('\n')
   files.pop()
   return files

def load_file(file_path: str) -> file_item:

    is_dir = path.isdir(file_path.replace('\ ', ' '))

    # print(f"{'Dossier :' if is_dir else 'Fichier :'} {file_path}")
    type = file_type.DIR if is_dir else file_type.FILE

    file_name = file_path.split('/').pop() if not is_dir else file_path+'/'

    node = file_item(file_name, type, file_path, [])

    if is_dir:
        sub_files = list_dir(format_path(f'{file_path}'))

        for sub_file in sub_files:
            node.add_child(load_file(format_path(path.join(f'{file_path}/', sub_file))))

    return node

def read_root(root: file_item):

    childs = root.get_childs()

    if root.type == file_type.DIR:
        with open ('output.txt', 'a') as output:
            output.write('------------------------------------------------- \n')
            output.write(f' [+] {root.name} ({root.number_duplicates}) : \n')
            output.close()

    for child in childs:
        if child.type != file_type.DIR:
            with open ('output.txt', 'a') as output:
                output.write(f' -> {child.name}\n')
                output.close()
        read_root(child)

