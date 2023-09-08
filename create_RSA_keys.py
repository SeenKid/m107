# pip install cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Générer une paire de clés RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Exposant public 
    key_size=2048  # Taille de clé 
)

# Sérialiser la clé privée
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Sérialiser la clé publique
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Sauvegarder les clés dans des fichiers
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_pem)

with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(public_pem)
