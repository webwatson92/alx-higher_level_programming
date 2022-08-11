#!/usr/bin/phthon3
with open('ali.jpg', 'rb') as rf:
    with open('ali_cp.jpg', "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



        """ for line in rf:
            wf.write(line) """

    
    """ for line in f:
        print(line, end="") """
    """ size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end="*")

    f_contents = f.read(size_to_read)
    print(f_contents) """