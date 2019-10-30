dict_a = {
    "name" : "javamix",
    "type" : "human",
    "type" : "flower"
}

print(dict_a)

print(dict_a['type'])

dict_a['type'] = 'animal'

print(dict_a)
print(len(dict_a))

dictionary = {}

print(dictionary)

dictionary["age"] = 2
dictionary["name"] = 'javamix'

print(dictionary)

key = input("input key :")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않은 키")

dictionary.get()