# b=8
# def func():
#     a=7
#     print(a)
#     print(b)
#
# func()


#Local scope


# def func(a=2):
#     print(a)
#     a=1
#     print(a)
#
# func()

#Enclosing scope

a=5
def red():
    a=1
    def blue():
        b=2
        print(a)
        print(b)
    blue()

    print(a)

red()
print(a)


# Global Scope

# a=1
# def counter():
#     a=2
#     print(a)
# counter()
# print(a)


# a=1
#
# def counter():
#     global a
#     a=2
#     print(a)
#
# counter()


# Non local keyword
# def red():
#                 a=1
#                 def blue():
#                         a=2
#                         b=2
#                         print(a)
#                         print(b)
#                 blue()
#                 print(a)
# red()


# def red():
#                 a=1
#                 def blue():
#
#                                 nonlocal a
#                                 a=2
#
#                                 b=2
#                                 print(a)
#                                 print(b)
#                 blue()
#                 print(a)
# red()


