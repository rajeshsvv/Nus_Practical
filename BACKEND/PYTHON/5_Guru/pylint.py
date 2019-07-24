import string
import pdb

shift = 3

choice = input("Would you like to encode or decode?:\t")
word = input("Please enter text:\t")
letters = string.ascii_letters+string.punctuation+string.digits
encoded = ""
if choice == "encode":
    breakpoint()
    for letter in word:
        if letter == "":
            encoded = encoded+" "
            breakpoint()
        else:
            x = letters.index(letter)+shift
            encoded = encoded+letters[x]

if choice == "decode":

    for letter in word:
        if letter == "":
            encoded += ""
        else:
            x = letters.index(letter)-shift
            encoded = encoded+letters[x]
print(encoded)

breakpoint()

print(dir(pdb))
print(help(pdb))

