from unittest import TestCase
from write import write_file

class WriteTest(TestCase):
    
    def testIfWritesProperly(self):
        try:
            write_file("./a.txt", "Hello World")

            with open("./a.txt", mode="r") as r:
                lines = r.readlines()

                self.assertEqual(lines, ["Hello World"], msg="Make sure you're using the correct mode. You should overwrite any existing file, not append.")
        except FileNotFoundError as e:
            self.fail(msg="File not found %s" % e)
        except FileExistsError as e:
            self.fail(msg="Make sure you're using the correct mode %s" % e)