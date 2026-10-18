# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# Try to read the file; if it's missing, print a message instead of crashing
try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found: records.txt")



#with open("records.txt") as f: # this file does not exsists in folder TO FIX IT ILL CAHNGE THIS INTO COMMENT
    #print(f.read())
