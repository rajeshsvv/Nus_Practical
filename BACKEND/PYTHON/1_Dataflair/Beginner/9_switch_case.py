#   Python does not have a switch-case construct. Along with this,
#   we will see how to work a loophole for Python switch case statement

#   we can impliment switch case statements by with classes or with functions or dictionaries

# using dictionaries

# def week(i):
#     switcher={
#         0:"saturday",
#         1:"monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#     }
#     return switcher.get(i,"Invalid day of the week")
#
# print(week(3))
# print(week(7))


#   using functions and lambdas
def zero():
        return 'zero'
def one():
        return 'one'
def indirect(i):
        switcher={
                0:zero,
                1:one,
                2:lambda:'two'
                }
        func= switcher.get(i,lambda :'Invalid')
        return func()

print(indirect(4))

print(indirect(2))

print(indirect(1))

print(indirect(0.5))

