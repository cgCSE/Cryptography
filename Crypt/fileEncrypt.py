from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()


# Save the encryption key to a file
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

    
# Encrypt a file
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)



# Usage
if __name__ == '__main__':
    key = generate_key()
    key_file = 'encryption_key.key'
    save_key(key, key_file)

    input_file = 'passwords.txt'
    encrypted_file = 'encrypted_file.txt'

    encrypt_file(input_file, encrypted_file, key)
    print(f"File '{input_file}' encrypted to '{encrypted_file}'")