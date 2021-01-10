alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar_cypher(text, shift, direction):
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    text_message = ""
    for char in text:
        if char not in alphabet:
            text_message += char
        else:
            cipher_char = alphabet[shift + int(alphabet.index(char))]
            text_message += cipher_char
    print(f"The {direction}d text is {text_message}")



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
caesar_cypher(text, shift, direction)