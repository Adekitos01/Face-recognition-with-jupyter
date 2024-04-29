from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


from src import HybridCipher
import sys


class HybridizedAlgorithm():

    def __init__(self) -> None:
        self.rsa_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

        self.rsa_public_key = self.rsa_private_key.public_key()
    
    def get_instance_attributes(self):
        print(f"Private key: {self.rsa_private_key}\nPublic key: {self.rsa_public_key}")
        return

    def encrypt_data(self, data: dict) -> str:
        self.encrypted_data = HybridCipher().encrypt(
            rsa_public_key=self.rsa_public_key, 
            data=data
        )
        return self.encrypted_data

    def decrypt_data(self, encrypted_data: str) -> dict:
        self.decrypted_message = HybridCipher().decrypt(
            rsa_private_key=self.rsa_private_key,
            cipher_text=encrypted_data
        )
        return self.decrypted_message




if __name__ == "__main__":
    hybrid_algorithm = HybridizedAlgorithm()

    input_file = input("Enter your file name: ")
    # input_file = open('iot-data.json')
    file_type = input_file.split(".")[1]
    # data = json.load(input_file)
    # file_name = input("Enter your file name: ")
    file = open(input_file)
    data = file
    # print(type(file))

    enc_data = hybrid_algorithm.encrypt_data(data=file_type)
    dec_data = hybrid_algorithm.decrypt_data(enc_data)

    # key = b'71ae0915dace4d928a8baa602f291df6'
    # print(key)
    while True:
        print('''
            1.) Encrypt?
            2.) Decrypt?
            3.) Exit program
        ''')

        choice = input('Enter your choice number: ')

        if choice == '1':
            print(f"Encrypted data: {enc_data}")
        elif choice == '2':
            print(f"Decrypted data: {dec_data}")
        elif choice == '3':
            sys.exit()

# encodeText()