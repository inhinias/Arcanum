from cx_Freeze import setup, Executable

setup(name='Axon',version='1.0A',description='A password encrypter which stores them in a databse',executables = [Executable("index.py")])