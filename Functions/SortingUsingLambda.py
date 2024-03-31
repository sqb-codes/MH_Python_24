data = [[104,"John"],[103,"Shawn"],[110,"Nick"],[106,"Adam"]]

print(sorted(data)) # it will sort based on 0th index

print(sorted(data, key=lambda x : x[1])) # it will sort based on 1st index

data = [
    {"id":104,"name":"Ravi"},
    {"id":109,"name":"Akash"},
    {"id":110,"name":"Vaibhav"},
    {"id":107,"name":"Sachin"},
]

print(sorted(data, key=lambda x : x["id"])) # it will sort according to id
print(sorted(data, key=lambda x : x["name"])) # it will sort according to name
