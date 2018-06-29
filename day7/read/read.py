
# Complete the read function and run the tests
def read_file(filename):
    # Your code here
    # replace this return with something 
    # more proper

    with open(filename, mode="r") as r:
        txt = ""
        # for line in r:
        #     txt += line
        
        # return txt

        line = r.readline()
        while line:
            txt += line
            line = r.readline()
        return txt