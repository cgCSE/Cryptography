import random
import string

def generate_random_password(length=15):
    """Generates a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_passwords(filename, passwords):
    """Saves a list of passwords to the specified file."""
    with open(filename, 'a') as file:  # Open file in append mode
        for password in passwords:
            file.write(password + '\n')

def main():
    password_file = 'passwords.txt'
    
    while True:
        try:
            # Prompt user for input lengths
            lengths_input = input("Enter password lengths (comma-separated) or type 'exit' to quit: ")
            if lengths_input.lower() == 'exit':
                break
            
            lengths = [int(length.strip()) for length in lengths_input.split(',')]
            
            if not lengths:
                print("No lengths provided.")
                continue
            
            num_passwords = 10  # Number of passwords to generate per length

            # Generate and save passwords for each length
            for length in lengths:
                if length < 1:
                    print(f"Invalid length {length}. Must be greater than 0.")
                    continue
                
                print(f"Generating {num_passwords} passwords of length {length}...")
                passwords = [generate_random_password(length) for _ in range(num_passwords)]
                save_passwords(password_file, passwords)
                print(f"Generated and saved {num_passwords} passwords of length {length} to '{password_file}'")
        
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers for password lengths.")

if __name__ == '__main__':
    main()
