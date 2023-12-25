import hashlib
from files_operations import format_path
BUF_SIZE = 65536

def get_hash_file(file_path: str) -> str:

   sha_256 = hashlib.sha256()
   file_path = file_path.replace('\\','')
   with open(file_path, 'rb') as f:

       while True:

           data = f.read(BUF_SIZE)

           if not data:
               break

           sha_256.update(data)
       return sha_256.hexdigest()
