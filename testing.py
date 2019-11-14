from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

private_Key =RSA.generate(1024)

print(private_Key)

