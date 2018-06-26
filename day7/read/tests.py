from unittest import TestCase
from read import read_file

class ReadTest(TestCase):
    
    def testIfReadProperly(self):
        contents = read_file("./testfile1.txt")

        self.assertEqual("""Hello World""", contents, "Contents read from testfile1.txt are not as expected")

        contents = read_file("./testfile2.txt")

        self.assertEqual("""Hello World
1234
Wow""", contents, "Contents read from testfile2.txt are not as expected")