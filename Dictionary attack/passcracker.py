import hashlib

def crackHash(inputPass):
    try:
        passFile = open('wordlist.txt', 'r')
    except FileNotFoundError:
        print('Could not find file: wordlist.txt.')
        return

    for password in passFile:
        encodedPass = password.encode('utf-8')
        digest = hashlib.md5(encodedPass.strip()).hexdigest()
        if digest == inputPass:
            print('Password Found: ' + password.strip())
            return
    print('Password not found.')

def main():
    try:
        hashFile = open('hashes.txt', 'r')
    except FileNotFoundError:
        print('Could not find file: hashes.txt.')
        return

    for hash in hashFile:
        hash = hash.strip()
        print(f'Cracking hash: {hash}')
        crackHash(hash)

if __name__ == '__main__':
    main()