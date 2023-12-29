from files_operations import delete_file

def remove_duplicates(duplicates : dict) -> None:
	for duplicate in duplicates:
         duplicate_file_to_delete = duplicates[duplicate][0]
         delete_file(duplicate_file_to_delete)

