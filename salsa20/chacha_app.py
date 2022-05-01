from chacha_with_viz import *

def main():
    key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f' \
          b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
    nonce = b'\x00\x00\x00\x00\x00\x00\x00\x4a\x00\x00\x00\x00'
    iv = 1
    done = False
    while not done:
        plaintext = input("Enter text to encrypt (or quit to end): ")
        if plaintext.lower() == 'quit':
            print("Thanks for encrypting with ChaCha20!")
            done = True
        else:
            try:
                plaintext = plaintext.encode('UTF-8')
                result = encrypt(key, nonce, plaintext, iv)
                print("Result is", result)
            except ValueError as err:
                print(err)
        print()


if __name__ == '__main__':
    main()
