#!usr/bin/python3
#0-read_file
#elhadjyoussoufo@gmail.com

def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

