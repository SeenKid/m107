# pip install cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Charger la clé privée depuis le fichier
with open("private_key.pem", "rb") as private_key_file:
    private_pem = private_key_file.read()
    private_key = serialization.load_pem_private_key(private_pem,password=None) # pas de mot de passe

# Charger la clé publique depuis le fichier
with open("public_key.pem", "rb") as public_key_file:
    public_pem = public_key_file.read()
    public_key = serialization.load_pem_public_key(public_pem)

# Message à signer
message = b"ce messade doit se faire signer"

# Signature numérique
signature = private_key.sign(message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())

# Vérification de la signature
try:
    public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
    print("La signature est valide.")
except cryptography.exceptions.InvalidSignature:
    print("La signature est invalide.")