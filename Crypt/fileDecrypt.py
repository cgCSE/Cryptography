from cryptography.fernet import Fernet

# Load the encryption key from a file.
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()


# Decrypt a file and return the decrypted data.
def decrypt_file(input_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    return fernet.decrypt(encrypted_data)

def main():
    key_file = 'encryption_key.key'
    encrypted_file = 'encrypted_file.txt'
    
    try:
        key = load_key(key_file)
        
        # Decrypt the file
        decrypted_data = decrypt_file(encrypted_file, key)
        
        # Handle the decrypted data securely
        # For example, you could print it or save it securely after confirmation
        action = input("Decrypted data is ready. Would you like to save it to a file? (yes/no): ").strip().lower()
        if action == 'yes':
            output_file = input("Enter the name for the decrypted file: ").strip()
            with open(output_file, 'wb') as file:
                file.write(decrypted_data)
            print(f"Decrypted data saved to '{output_file}'")
        else:
            print("Decrypted data not saved.")
    
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
