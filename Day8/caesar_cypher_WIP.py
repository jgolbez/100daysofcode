alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  encrypt_list = []
  text_list = list(text)
  encrypt_message = ""
  for char in text_list:
    #Capture non-alphabet characters
    if char not in alphabet:
      encrypt_list.append(char)
    else:
      #Start with empty list, so append encoded data to list
      encrypt_char = alphabet[shift + int(alphabet.index(char))]
      encrypt_list.append(encrypt_char)
  print(f"The encoded text is {encrypt_message.join(encrypt_list)}")

def decrypt(text, shift):
  decrypt_list_index = -1
  decrypt_list = list(text)
  decrypt_message = ""
  for char in decrypt_list:
    #Do not attempt to convert non-alphabet characters
    if char not in alphabet:
      continue
    else:
    #Starting with populated list from input so must replace/remove old characters
      decrypt_char = alphabet[int(alphabet.index(char)) - shift]
      #Iterator over index allows us to replace characters in list in-line as it decodes
      decrypt_list_index += 1
      decrypt_list[decrypt_list_index] = decrypt_char
        
  print(f"The decoded text is {decrypt_message.join(decrypt_list)}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("Not a valid choice")
