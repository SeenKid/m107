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

# generate a key
key = RSA.generate(1024)
print(key)

# export keys
k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')

# open files
with open('private.pem','w') as kf:
	kf.write(k.decode())
	kf.close()

with open('public.pem','w') as pf:
	pf.write(p.decode())
	pf.close()
