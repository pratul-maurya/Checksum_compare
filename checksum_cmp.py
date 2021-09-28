import sys
import hashlib
  
 
def hashfile_sha256(file): """Program to calculate the md5 and sha256 hash"""
  
    # An arbitrary (but fixed) buffer size (change accordingly)
    # 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536
  
    # Initializing the sha256() method
    sha256 = hashlib.sha256()
  
    # Opening the file provided as
    # the first commandline argument
    with open(file, 'rb') as f:
         
        while True:
             
            # reading data = BUF_SIZE from
            # the file and saving it in a
            # variable
            data = f.read(BUF_SIZE)
  
            # True if eof = 1
            if not data:
                break
      
            # Passing that data to that sh256 hash
            # function (updating the function with
            # that data)
            sha256.update(data)
  
      
    # sha256.hexdigest() hashes all the input
    # data passed to the sha256() via sha256.update()
    # Acts as a finalize method, after which
    # all the input data gets hashed hexdigest()
    # hashes the data, and returns the output
    # in hexadecimal format
    return sha256.hexdigest(
  
  
def hashfile_md5(file):
  
    # A arbitrary (but fixed) buffer
    # size (change accordingly)
    # 65536 = 65536 bytes = 64 kilobytes
    BUFF_SIZE = 65536
  
    # Initializing the sha256() method
    md5 = hashlib.md5()
  
    # Opening the file provided as
    # the first commandline argument
    with open(file, 'rb') as f:
         
        while True:
             
            # reading data = BUF_SIZE from
            # the file and saving it in a
            # variable
            data = f.read(BUFF_SIZE)
  
            # True if eof = 1
            if not data:
                break
      
            # Passing that data to that sh256 hash
            # function (updating the function with
            # that data)
            md5.update(data)
  
      
    # sha256.hexdigest() hashes all the input
    # data passed to the sha256() via sha256.update()
    # Acts as a finalize method, after which
    # all the input data gets hashed hexdigest()
    # hashes the data, and returns the output
    # in hexadecimal format
    return md5.hexdigest()    
 
# Calling hashfile() function to obtain hashes
# of the files, and saving the result
# in a variable  
f1_hash = hashfile_sha256(sys.argv[1])
f2_hash = hashfile_sha256(sys.argv[2])
  
m1_hash = hashfile_md5(sys.argv[1])
m2_hash = hashfile_md5(sys.argv[2])

# Doing primitive string comparison to
# check whether the two hashes match or not
if ((f1_hash == f2_hash) and (m1_hash==m2_hash)):
    print("Both files are same")
    print(f"Hash: {f1_hash}")
 
else:
    print("Files are different!\n")
    print(f"Hash of File 1 SHA-256: {f1_hash}")
    print(f"Hash of File 2 SHA-256: {f2_hash}\n")
    print(f"Hash of File 1 MD5: {m1_hash}")
    print(f"Hash of File 2 MD5: {m2_hash}")
