alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  encrypt_list = []
  text_list = list(text)
  encrypt_message = ""
  #DEBUG - print(text_list)
  for char in text_list:
    if char not in alphabet:
      encrypt_list.append(char)
    else:
      #DEBUG - print(int(alphabet.index(char)))
      encrypt_char = alphabet[shift + int(alphabet.index(char))]
      encrypt_list.append(encrypt_char)
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
  print(f"The encoded text is {encrypt_message.join(encrypt_list)}")
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)