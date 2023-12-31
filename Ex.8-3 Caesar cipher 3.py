alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# Mine:
# def caesar(plain_text, shift_amount):
#   if direction == "encode":
#     output_text = ""
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       output_text += alphabet[new_position]
#     print(f"The encoded text is {output_text}")

#   elif direction == "decode":
#     output_text = ""
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
#       output_text += alphabet[new_position]
#     print(f"The decoded text is {output_text}")
# caesar(plain_text = text, shift_amount = shift)

# Not mine:
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text = text, shift_amount = shift, cipher_direction = direction)