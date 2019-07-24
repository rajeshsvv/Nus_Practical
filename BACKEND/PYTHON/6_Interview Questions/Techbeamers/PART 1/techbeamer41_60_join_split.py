                             # chr and ord
'''
print(chr(122))
print(ord('V'))
test_str = 'Programming    '
test_str="  programming"
# The trailing whitespaces are excluded
print(test_str.lstrip())
'''

                                # isalpha and isnumeric

'''
string='AbWCDCEFGH'
number='12345678'
print(string.isalpha())
print(number.isnumeric())
'''

                                    # join vs split

'''
str = 'pdfcsvjson'
str=".".join(str)
print(str)
print(str.split(","))
'''

                                        # Title() method

# to convert the first letter in each word to capital format while the rest are in lowercase

# str="amrutam"
# print(str.title())


#46

str="Hello Rajesh How are you"

print(str.split(" "))
print("-".join("Hello Rajesh How are you"))

