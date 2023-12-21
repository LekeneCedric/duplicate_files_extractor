import hashfile

def check_duplicates_files(file_path_1: str, file_path_2: str) -> bool:

    f1_hash = hashfile.get_hash_file(file_path_1)

    f2_hash = hashfile.get_hash_file(file_path_2)

    return f1_hash == f2_hash
