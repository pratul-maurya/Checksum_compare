import sys
import hashlib
  
 
def hashfile_sha256(file):

  
  
def hashfile_md5(file):
  
  
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
