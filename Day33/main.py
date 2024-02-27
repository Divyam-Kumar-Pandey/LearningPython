info = {
    'name' : 'Karan',
    'age' : 19,
    'eligible' : True
}

print(info['name']) # throws error if not found
print(info.get('name')) # Gives 'None' if not found

print(info.keys())
print(info.values())
print(info.items())

for key in info.keys():
    print(info.get(key))

for key, value in info.items():
    print(f"{key} : {value}")