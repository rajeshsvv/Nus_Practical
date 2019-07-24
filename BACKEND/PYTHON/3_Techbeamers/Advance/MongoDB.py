from pymongo import MongoClient
con=MongoClient("localhost",27017)
con=MongoClient()


# 2- How To Create A Database In MongoDB?
db=con.testdb

# print(type(db))


# 3- How To Access A Collection In MongoDB?

my_coll=db.coll_name


print(my_coll)


# 4- How To Add Documents To A Collection?

emp_details={'name':"rajesh","address":"Karavali",id:"101"}

rec_id = my_coll.insert_many(emp_details)


# 5- How To Query Data In A Collection?


# The Python MongoDB driver also gives you a method <find()> to query data from any MongoDB collection.

# testdb.coll_name.find()

# testdb.coll_name.find()

# testdb.coll_name.find().pretty()
# {
#     "id":"",
#     "name":"",
#     "address":"",
#     "id":""
# }


# 6- How To Update Data In A Collection?

# To modify a collection, use any of the following Python MongoDB methods.
#
# <update_one()>,
# <update_many()>.


# 7- How To Remove Data From A Collection?
# Same like the update, here is a list of methods to delete the documents.
#
# <delete_one()>,
# <delete_many()>

ret=db.posts.delete_many({"category":"general"})



# Real Time Example

from pymongo import MongoClient


#connect to the MongoDB.
con=MongoClient("localhost",1080)

#Access the testdb database and the emp collection.
db=con.testdb.emp

#create dictionary to hold the emp collection

# create dictionary

emp_details={}

flag=True

while(flag):

    # ask for input
    emp_name,emp_addr,emp_id=input("Enter Emp Name,Address, and id: ").split(",")

    emp_detail={'name':emp_name,"address":emp_addr,"id":emp_id}

    # insert the record

    db.insert(emp_details)

    # Ask from user  if he wants to contnue to insert the records?

    flag=input("Enter another record?")
    if(flag[0].upper()=="Y"):
        flag=False

# find all documents

ret=db.find()

print()

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


# display the documents from collection

for record in ret:
    #print out the document
    print(record['name']+',',record['address']+',',record[id])

print()


con.close()




