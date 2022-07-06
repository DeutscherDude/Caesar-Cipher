#Day_8_Caesar_Cipher-Full

from Caesar_Cipher_Art import logo

alphabet = [chr(n) for n in range(97, 123)]

signs = [chr(n) for n in range(33, 48)] + [chr(n) for n in range(91, 97)] + [chr(n) for n in range(161, 188)]

def caesar(message, shift, direction):
    crypted = []

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    if direction == "decode":
        shift *= -1

    for letter in message:
        if alphabet.__contains__(letter):
            new_position = alphabet.index(letter) + shift

            if new_position >= len(alphabet):
                crypted += alphabet[(new_position - len(alphabet))]
            
            else:
                crypted += alphabet[new_position]
        elif signs.__contains__(letter):
            crypted += letter

    crypted = ''.join(str(e) for e in crypted)
    print(f"Your decrpted message is: {crypted}")

print(logo)      


while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt \n")
    message = input("Give me a message you would like to encrypt\decrypt:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message, shift, direction)

    choice = input("Do you wish to continue? 'Y/N'\n").lower()

    if choice == "y":
        True
    elif choice == 'n':
        print("Goodbye 😊")
        break
    else:
        print("Incorrect choice, running the program again :^).")


