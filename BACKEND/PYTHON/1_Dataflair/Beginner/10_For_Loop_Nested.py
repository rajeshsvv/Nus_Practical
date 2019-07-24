#       For Loop, Python While Loop, Python Loop Control Statements, and Nested For Loop in Python

#Python For Loop
#Python While Loop
#Python Loop Control Statements
#Nested For Loop in Python


# print 1 to 100 numbers
# for i in range(1,100):
#     print(i," ",end="")


#    While loop
#A while loop in python iterates till its condition becomes False.
#In other words, it executes the statements under itself while the condition it takes is True

#while loop can be implimented in threee ways

# An infinite loop
# The else statement for while loop
# Single statement while


# a=3
# while a>0:
#     print(a)
#     a-=1
    # if a==1:
    #     break
    # # else:
    # #     print("Reached 0")



#                                          3. Python For Loop


#   Python for loop can iterate over a sequence of items

# for i in range(3):
#     print(i+1)

# print(range(20))
# print(list(range(1,3)))
# print(list(range(2,12,2)))
# print(list(range(12,2,-2)))
# print(list(range(12,2)))            #[]
# print(list(range(2,12,-2)))         #[]
#print(list(range(12,2,2)))          #[]


# for i in (1,2,3,6,7,6,7,8):             #for duplicate elements set it will give unique values list and tuple duplicate values
#     print(i)


# for i in 'wisdom':
#     print(i)




#   c. Iterating on indices of a list or a similar construct

# list=["Romania","Kalkutta","Singapur"]
# for i in range(len(list)):
#     print(list[i])



# for i in range(10):
#     print(i)
#     if(i==7):
#         break
#     else:
#         print("Reached else")

# i=6
# while(i>0):
#   j=6
#   while(j>i):
#     print("*",end=' ')
#     j-=1
#   i-=1
#   print("\n",end='')



#   5. Loop Control Statements in Python

# break continue pass

#   When you put a break statement in the body of a loop, the loop stops executing,
#   and control shifts to the first statement outside it. You can put it in a for or while loop.

# for i in 'break':
#   print(i)
#   if i=='a': break;


#   b. continue statement
# When the program control reaches the continue statement, it skips the statements after ‘continue’.
# It then shifts to the next item in the sequence and executes the block of code for it. You can use it with both for and while loops.

i=0
while i<8:
    i+=1
    print(i)
    if i==6:
        continue
        print(i)


#   c. pass statement
# In Python, we use the pass statement to implement stubs. When we need a particular loop, class, or function in our program,
# but don’t know what goes in it, we place the pass statement in it. It is a null statement.
# The interpreter does not ignore it, but it performs a no-operation (NOP).