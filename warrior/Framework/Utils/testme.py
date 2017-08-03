
import unittest 
from os import sys, path 
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
import string_Utils 
import file_Utils as FU

class TestDirMethods(unittest.TestCase): 
    def test_glob(self):
        tc =  path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/Warriorspace/Testcases/Samples/*'
        self.assertTrue(len(FU.get_xml_files_in_path(tc)) > 0) 

if __name__ == '__main__':
    unittest.main() 
