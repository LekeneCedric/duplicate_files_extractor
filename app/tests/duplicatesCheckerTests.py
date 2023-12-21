import unittest
import os
import sys

sys.path.append('../../app/src/actions/')

from duplicates_checker import check_duplicates_files

class TestDuplicatesChecker(unittest.TestCase):

    def test_can_check_if_two_duplicates_files_have_same_hashes(self):
        """
		 Test that 2 duplicates files have same hashes
    	"""
        sut = self.build_system_under_test()

        files_is_duplicated = check_duplicates_files(sut["file1_path"], sut["file2_path"])
        os.remove(sut['file1_path'])
        os.remove(sut['file2_path'])

        self.assertTrue(files_is_duplicated)

    def build_system_under_test(self):

        both_files_content = 'files_content'

        file1_path = 'file1.txt'
        file2_path = 'file2.txt'

        file1 = open(file1_path, 'w')
        file1.write(both_files_content)
        file1.close()

        file2 = open(file2_path, 'w')
        file2.write(both_files_content)
        file2.close()

        return {
			"file1_path": file1_path,
            "file2_path": file2_path,
		}

if __name__ == "__main__":

    unittest.main()
