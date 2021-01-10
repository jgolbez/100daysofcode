alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar_cypher(text, shift, direction):
    if direction == "decode":
        shift *= -1
    text_message = ""
    for char in text:
        if direction == "decode" and char not in alphabet:
            text_message += char
        elif direction == "encode" and char not in alphabet: 
            text_message += char
        else:
            cipher_char = alphabet[shift + int(alphabet.index(char))]
            text_message += cipher_char
    print(f"The {direction}d text is {text_message}")


def encrypt(text, shift):
  encrypt_message = ""
  for char in text:
    #Capture non-alphabet characters
    if char not in alphabet:
      text += char
    else:
      #Start with empty list, so append encoded data to list
      encrypt_char = alphabet[shift + int(alphabet.index(char))]
      encrypt_message += encrypt_char
  print(f"The encoded text is {encrypt_message}")

def decrypt(text, shift):
  decrypt_message = ""
  for char in text:
    #Do not attempt to convert non-alphabet characters
    if char not in alphabet:
      continue
    else:
    #Starting with populated list from input so must replace/remove old characters
      decrypt_char = alphabet[int(alphabet.index(char)) - shift]
      decrypt_message += decrypt_char
        
  print(f"The decoded text is {decrypt_message}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
caesar_cypher(text, shift, direction)