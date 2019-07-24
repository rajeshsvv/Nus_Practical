# <file.closed>	For a closed file, it returns true whereas false otherwise.
# <file.mode>	It returns the access mode used to open a file.
# <file.name>	It returns the name of a file.
# <file.softspace>	It returns a boolean to suggest if a space char will get added before printing another value
#                     in the output of a <print> command.

import os

"""

#Open a file in write and binary mode.
fob = open("D:\\DEVELOPER\\BACKEND\\PYTHON\\PRACTICE\\THEORY\\Imp bits.txt", "r")

#Display file name.
print("File name: ", fob.name)
#Display state of the file.
print("File state: ", fob.closed)
#Print the opening mode.
print("Opening mode: ", fob.mode)
# #Output the softspace value.
# print("Softspace flag: ", fob.softspace)

"""


fob = open("C:\\Users\\rajeshvs\\Desktop", "w+")

print(chr('a'))
with open('app.log', 'w', encoding = 'utf-8') as f:
   #first line
   f.write('my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

with open('app.log', 'r', encoding = 'utf-8') as f:
   content = f.readlines()

for line in content:
   print(line)
fob.close()