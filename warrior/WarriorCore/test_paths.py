
import unittest 
import os,sys
import glob
from xml.etree import ElementTree
from xml.etree.ElementTree import tostring
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Framework/")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Framework/Utils")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Framework/ClassUtils")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Framework/OSS")
import Utils 
import Framework
import Framework.OSS
from Utils import xml_Utils
import copy


class TestExpandSuites(unittest.TestCase):
    def test_project_expansion(self):
        project_filepath = '/home/khusain/warriorframework/wftests/warrior_tests/projects/pj_glob_files.xml'
        print Utils.xml_Utils.get_expanded_file_elements(project_filepath)
        return 

    
    def test_suite_expansion(self):
        # TODO must use relative path names here .... 
        dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print dirname + "/../../wftests/warrior_tests/suites/framework_tests"
        project_filepath = '/home/khusain/warriorframework/wftests/warrior_tests/suites/framework_tests/ts_glob_files.xml'
        print Utils.xml_Utils.get_expanded_file_elements(project_filepath,'Testcase')
        return 


    def saveme(self):
        testsuites = root.find('Testsuites') 
        t_list = testsuites.findall('Testsuite') 
        # -------------------------------------------------
        # this is the entry point of the function... 
        # need the name of the project file, and the root
        # -------------------------------------------------
        print t_list
        new_list = [] 

        for tx in t_list: 
            txname = tx.find('path').text 
            if txname.find('*') < 0: 
                print "No glob found...", txname 
                new_list.append(copy.copy(tx))
                continue
            xstr = os.path.dirname(tx.find('path').text)     # Get the path name 
            dpath =  Utils.file_Utils.getAbsPath(xstr, project_dir) + '/*'  
            files = [ x for x in glob.glob(dpath) if x.find(".xml") > 0 ] 
            if len(files) > 1:
                for fn in files:  
                    tn = copy.deepcopy(tx) 
                    tn.path = fn 
                    tn.find('path').text = fn 
                    new_list.append(tn) 
                    print "added ...", fn,tn.path
                   

        for tx in new_list:
            print tx,tx.find('path').text
        # return new_list here.


if __name__ == '__main__':
    unittest.main()

