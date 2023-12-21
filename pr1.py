print("hello")

a = 5 
assert a < 10, "a value is too small"

qty = 10 
product = "cucumber"

my_order = "i want to pay for {} products and product name is {}"
print(my_order.format(qty,product))

#list
x = [1,2,3,4,5]
y = [22,44,23,55]

z = x+y
#print(z)
for i in y:
    x.append(i)
print(x)

#tuple
tupl1 = (1,3,4,5,6,7)
print(tupl1)

lst = list(tupl1)
lst[2] = "het"
tupl1 = tuple(lst)

print(tupl1)

#SET
set = {1,2,3,2,"het shah"}
print(set)

set.add("orange")
print(set)
set2 = {"fruits","cheery","banana"}
set.update(set2)
set.remove("banana")
print(set)

x1 = set.intersection_update(set2)
print(x1)

set.symmetric_difference_update(set2)
print(set)

dict1 = {
    "name": "Het",
    "surname" : "Shah",
    "rollno" : 31
}
print(dict1)

#copy of dict
mydict = dict1.copy()
print(mydict)

#add
mydict["value"] = "key"
print(mydict)

#update
mydict.update({'value' : 0})
print(mydict)

myfamily = {
    "child1" : {
        "name" : "het",
        "id" : "hetshah1309@gmail.com"
    },
    "child2" : {
        "name" : "akash",
        "id" : "akashbhavshar11@gmail.com"
    }
}

print(myfamily)