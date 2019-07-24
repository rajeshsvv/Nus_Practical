# Python Programming Language doesn’t have arrays.
# A Python list can be seen as a collection of values
# Remember once again, you don’t need to declare the data type, because Python is dynamically-typed.

# colors=['red','green','blue']
# print(colors)
#
# languages=[['English'],['Gujarati'],['Hindi'],['Romanian','Spanish']]
# print(languages)

# languages=[['English'],['Gujarati'],['Hindi'],'Romanian','Spanish']
# print(languages[:2])
#
# indices=['zero','one','two','three','four','five']
# print(indices[2:4])
# print(indices[1:-1])
# print(indices[:-2])

#   A list may also contain tuples or so.

# languages=[('English','Albanian'),'Gujarati','Hindi','Romanian','Spanish']
# print(languages[0])
#
# print(type(languages))
# languages[1]="Samira"
# print(languages)
                                        # 6    Reassigning the whole Python list


# colors=['caramel','gold','silver','occur']
# print(colors)
# colors[:2]=['bronze','silver']
# print(colors)
# colors[1]="gulabi"
# print(colors)
#
# colors=['caramel','gold','silver','bronze','holographi']
# del colors[1:3]
# print(colors)

                                        # 8     Multi dimensional list

# grocery_list=[['caramel','P&B','Jelly'],['onions','potatoes'],['flour','oil']]
# print(grocery_list[2])
#
# a=[[[1,2],[3,4],5],[6,7]]
# print(a[0][0][1])



#                                       10.     Python List Operations

#   a. Multiplication

# a=[3, 1, 2]
# a*=3
# print(a)


#   b. Membership

# p=2 in a
# print(p)
#
# q=8 not in a
# print(q)


                                        # 11    Iterating a list

# for i in [1,2,3,4,6,8,10]:
#          if i%2==0:
#                 print(f"{i} is composite\n")




#                                   12. Python List Comprehension


# even=[2*i for i in range(6)]
# print(even)
#
# even=[3**i for i in range(1,5) if i%2==0]
# print(even)


#                                   13. Built-in List Functions

# sum()          max()       min()              any()
# all()         list()      sorted()            len()


a=[1,2,3,9,5,6]

# print(sum(a))
# print(max(a))
# print(min(a))
# print(any(a))
# print(all(a))
# print(list(a))
# print(sorted(a))
# print(len(a))

b=['1','2','3']
# b=['i','','']
# print(sum(b))
# print(len(b))
# print(max(b))
# print(min(b))
print(any(b))
# print(all(b))
# print(list(b))
# print(sorted(a))    #It returns a sorted version of the list, but does not change the original one.


