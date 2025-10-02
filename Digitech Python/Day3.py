my_dict = {"name":"Phoenix","age":22,"tribe":"Somali"}
print(my_dict)

# my_dict.clear()
# print(my_dict)

backup = my_dict.copy()
print(backup)

keys = ["name","age","City"]
values = "unknown"
default = dict.fromkeys(keys, values)
print(default)

getting = backup.get("age")
print(getting)

key1 = backup.keys()
print(key1)

value1 = my_dict.values()
print(value1)

all_item = backup.items()
print(all_item)

popping = backup.pop("name")
print(popping)
print(backup)

popitem = my_dict.popitem()
print(popitem)
print(my_dict)

new_dict = {"name":"Xexers", "Country":"Kenya"}
setdefaulting = new_dict.setdefault("name", "Giriama")
print(setdefaulting)

updating = my_dict.update(new_dict)
print(my_dict)

new_keys = ["School", "Gender", "Class"]
new_values = ["Barani", "Female", 8]
complete_dict = dict(zip(new_keys, new_values))
print(complete_dict)