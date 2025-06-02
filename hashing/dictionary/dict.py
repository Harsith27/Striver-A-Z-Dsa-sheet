mydict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
#Accessing a value
print(mydict["name"])

#inserting a value
mydict["Pin"]=530011

#inserting multiple values
mydict["colors"]="blue",1,"yellow"

#accessing a multi valued iterable
print(mydict["colors"][1])

#changing a value
mydict["Pin"]=123

#dict constructor
mylist=[1,2,3,4,5,6]
print(dict(mylist))


#printing a dict
print(mydict)