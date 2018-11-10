#This file is being used for testing how to encrypt with gpg


from pathlib import Path
import gnupg

gpg = gnupg.GPG(gnupghome = str(Path.home()))
gpg.encoding = 'utf-8'
    
def generateKey(typeOfKey="RSA", length=1024):
        print("generating keys")
        inputData = gpg.gen_key_input(key_type=typeOfKey, key_length=length, name_real="ArcanumKey")
        key = gpg.gen_key(inputData)
        print(str(key))
        return key

def encrypt(theData, thePassphrase):
    encrypted = str(gpg.encrypt(data=theData, recipients=None, passphrase="password", symmetric=True))
    return encrypted
    
def decrypt(theData, thePassphrase):
    decrypted = gpg.decrypt(message=theData, passphrase=thePassphrase)
    return str(decrypted), decrypted.ok, decrypted.status 

def encryptFile(recipients, theData, thePassphrase):
    encrypted = str(gpg.encrypt_file(data=theData, recipient=None, passphrase=thePassphrase, symmetric=True))
    return encrypted
    
def decryptFile(theData, thePassphrase):
    decrypted = str(gpg.decrypt_file(data=theData, passphrase=thePassphrase))
    return decrypted.data, decrypted.ok, decrypted.status 


for i in range(10):
    theEncrypt = encrypt("test", "Password")
    print(theEncrypt)
    theDecrypt = decrypt(theEncrypt, "Password")
    print(theDecrypt)

