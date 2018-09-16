from pathlib import Path
import gnupg

class Encryption:
    def __init__(self):
        global gpg
        gpg = gnupg.GPG(gnupghome = str(Path.home()))
        gpg.encoding = 'utf-8'
    
    def generateKey(self, typeOfKey="RSA", length=8192):
        print("generating keys")
        inputData = gpg.gen_key_input(key_type=typeOfKey, key_length=length, name_real="ArcanumKey")
        key = gpg.gen_key(inputData)
        return key

    def encrypt(self, recipient, theData, thePassphrase):
        encrypted = str(gpg.encrypt(data=theData, recipients=None, passphrase=thePassphrase, symmetric=True))
        return encrypted
    
    def decrypt(self, theData, thePassphrase):
        decrypted = gpg.decrypt(data=theData, passphrase=thePassphrase)
        return str(decrypted), decrypted.ok, decrypted.status

    def encryptFile(self, recipients, theData, thePassphrase):
        encrypted = str(gpg.encrypt_file(data=theData, recipients=None, passphrase=thePassphrase, symmetric=True))
        return encrypted
    
    def decryptFile(self, theData, thePassphrase):
        decrypted = str(gpg.decrypt_file(data=theData, passphrase=thePassphrase))
        return decrypted