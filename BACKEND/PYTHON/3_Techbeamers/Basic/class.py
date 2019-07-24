# Python provides the “self” keyword to represent the instance of a class.
# It works as a handle for accessing the class members such as attributes from the class methods.

# What Is __init__ (Constructor) In Python?
# The “__init__()” is a unique method associated with every Python class.


# Create A BookStore Class In Python
class BookStore:
    noOfBooks = 0
    def __init__(self):
        print("__init__ constructor is called")

b1=BookStore()


# The Class Attributes
class BookStore:
    instances=0
    def __init__(self, attri1, attri2, attri3):
        self.attrib1 = attri1
        self.attrib2 = attri2
        self.attrib3 = attri3
        BookStore.instances+=1
b1 = BookStore("", "", "")
b2 = BookStore("","","")
b3 = BookStore("","","")

print("BookStore.instances", BookStore.instances)


# Create A BookStore Class In Python
class BookStore:
    noOfBooks=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        BookStore.noOfBooks +=1

    def bookInfo(self):
        print("Book Title",self.title)
        print("Book Author",self.author,"\n")

b1=BookStore("Great Expectations","Charles Dickens")
b2=BookStore("War and Peace","Leo Tolstoy")
b3=BookStore("MiddleMarch","George Eliot")

b1.bookInfo()
b2.bookInfo()
b3.bookInfo()

print(BookStore.noOfBooks)
print(BookStore.noOfBooks)
