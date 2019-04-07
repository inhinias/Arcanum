import pytest
from components import crypt

class Crytest():
    def test_encryption(self):
        test = crypt.Encryption.encrypt(self, theData="Test", password="Verify", recipients=None, useSymmetric=True)
        assert test == '-----BEGIN PGP MESSAGE-----\n\njA0ECQMCXyCLa4iM5zT/0jkBjU94YN0wBBdAw7pSUkGTHlFT/SpMRxGt66EwmmT7\ng5iyBig+3dhL7Y0g/v2MQOQIPcJC8/Jn05g=\n=pIBB\n-----END PGP MESSAGE-----\n'

    def test_decryption(self):
        test = crypt.Encryption.decrypt(self, theData='-----BEGIN PGP MESSAGE-----\n\njA0ECQMCXyCLa4iM5zT/0jkBjU94YN0wBBdAw7pSUkGTHlFT/SpMRxGt66EwmmT7\ng5iyBig+3dhL7Y0g/v2MQOQIPcJC8/Jn05g=\n=pIBB\n-----END PGP MESSAGE-----\n', passphrase="Verify", recipients=None, useSymmetric=True)
        assert test == 'Test'

    def test_genPassword():
        assert True

