from pathlib import Path
import gnupg

class Encryption:
    def __init__(self):
        global gpg
        gpg = gnupg.GPG(gnupghome = str(Path.home()))
        gpg.encoding = 'utf-8'
    
    def generateKey(self, type, length):
        print("generating")

    def encrypt(self, recipients, theData, thePassphrase):
        encrypted = str(gpg.encrypt(data=theData, recipient=recipients, passphrase=thePassphrase, symmetric=True))
        return encrypted
    
    def decrypt(self, theData, thePassphrase):
        decrypted = str(gpg.decrypt(data=theData, passphrase=thePassphrase))
        return decrypted

    def encryptFile(self, recipients, theData, thePassphrase):
        encrypted = str(gpg.encrypt_file(data=theData, recipient=recipients, passphrase=thePassphrase, symmetric=True))
        return encrypted
    
    def decryptFile(self, theData, thePassphrase):
        decrypted = str(gpg.decrypt_file(data=theData, passphrase=thePassphrase))
        return decrypted