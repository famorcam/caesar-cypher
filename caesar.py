import sys


def encrypt(message, k):
    key = int(k)
    # initializing an empty list to store our ascii numbers

    ascii_numbers = []
    # for loop to iterate over each character
    for letter in message:
        # only checking for lowercase letters
        if 'a' <= letter <= 'z':
            # retrieve ascii numbers with ord(letter), subtract ascii number 'a', (this gives us a relative position), add key
            # then take that result % 26, this in effect is our "wrapping around" logic
            # Lastly add the modded value to the ascii number of 'a', which in effect starts a count from the top of the alphabet

            # example where k = 10 and the letter is 'd'
             
            # 'd' - 'a' + 10 = 13
            # (100)-(97) + 10 = 13
            # 13 % 26 = 13
            # 13 + 97 = 110 (this value corresponds to 'n')

            # finally append each number to the ascii_number list
            ascii_numbers.append((ord(letter) - ord('a') + key) % 26 + ord('a'))

    # now that we have our ascii numbers we can convert them back into letters with chr()
    back_to_letters = []
    for number in ascii_numbers:
        back_to_letters.append(chr(number))
    
    # join the elemnts in the list back into a string   
    encrypted_message = ''.join(back_to_letters)
    return encrypted_message

def decrypt(encrypted_message, k):
    key = int(k)

    ascii_numbers = []
    for letter in encrypted_message:
        if 'a' <= letter <= 'z':
            # we are effectively doing the same logic as above 
            # however to unwind the encrypted message we substract the key
            # subtracting the key returns to the original ascii number
            ascii_numbers.append((ord(letter) - ord('a') - key) % 26 + ord('a'))

    back_to_letters = []
    for number in ascii_numbers:
        back_to_letters.append(chr(number))

    decrypted_message = ''.join(back_to_letters)
    return decrypted_message

if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)


    