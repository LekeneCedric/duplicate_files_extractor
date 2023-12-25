def println(str: str) -> None:
    print(f'{str}\n')

def extract_file_name_from_path(file_path: str) -> str:
    file_name = file_path.split('/')[-1].replace('\\','')
    return file_name
