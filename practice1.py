
# A practice of Arithmatic Operator
a = 15
b = 4

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a / b = {a / b}")
print(f"a % b = {a % b}")
print(f"a // b = {a // b}")
 
# comparison

print(f"a == b {a == b}")
print(f"a != b {a != b}")
print(f"a < b {a < b}")
print(f"a > b {a > b}")

# variable making

city = "Hyderabad"
temperature = 20
is_raining = True

print(f"city {city}, temperature {temperature}, raining {is_raining}")

# dictionary & sets

mydict = {
    "name" : "Anuj",
    "SirName" : "Sharma",
    "info" : {
        "Age" : 22,
        "Category" : "gen",
    }
}

#print(mydict)
print(mydict["name"])
print(list(mydict.keys()))

# if we do *print(mydict["name2"])* run terminal shows us error but if we put *print(mydict.get(name2))* then it will show "NOne" and the second approach will be a better approach always because first one will stop next other line codes, that make s your code unstable.

