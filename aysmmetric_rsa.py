
import rsa

(pubkey,privkey)=rsa.newkeys(1024)

print(privkey)
print(pubkey)
message=b'mytopsecret'

crypto=rsa.encrypt(message,pubkey)
print(crypto)
decrypt=rsa.decrypt(crypto,privkey)

print(decrypt.decode())



