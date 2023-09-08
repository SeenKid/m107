# import libs
import hashlib
from Crypto.PublicKey import RSA

# hash some text with md5
result = hashlib.md5(b'TextToHash').hexdigest()
print("\n" + result + "\n")

# hash some text with SHA256
result2 = hashlib.sha256(b'TextToHash').hexdigest()
print(result2 + "\n")

# hash some text with SHA1
result3 = hashlib.sha1(b'TextToHash').hexdigest()
print(result3 + "\n")
