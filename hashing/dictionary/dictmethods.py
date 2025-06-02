mydict={
    "name":"Harsith",
    "branch":"CSE",
    "Roll No":134
}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

letters=[[1,2],[3,4],[5,6]]

#Access a value of a key
print(mydict.get("name",2))

#Keys of the dictionary
print(mydict.keys())

#values of the dictionary
print(mydict.values())

#items or key value pairs of a dict
print(mydict.items())

#update method
mydict.update(letters)
print(mydict)

#delete or pop an item
print(mydict.pop("bench","key not found"))
print(mydict.pop("branch","key not found"))

#delete last item
print(mydict.popitem())
