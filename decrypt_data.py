import rsa
from cryptography.fernet import Fernet

# load the private key to decrypt the public key
prkey = open('privkey.key','rb')
pkey = prkey.read()
private_key = rsa.PrivateKey.load_pkcs1(pkey)

e = open('encrypted_key','rb')
ekey = e.read()

dpubkey = rsa.decrypt(ekey,private_key)

cipher = Fernet(dpubkey)

encrypted_data = open('encrypted_data','rb')
edata = encrypted_data.read()


decrypted_data = cipher.decrypt(edata)

print(decrypted_data.decode())