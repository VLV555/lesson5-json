import json
with open("users.json", "r") as f:
    users = json.load(f)
address = {}

# # Длинный путь:
# for user in users:
#     city = None
#     name = None
#     for keys,values in user.items():
#         # print(keys,values)
#         if keys == "address":
#             for keyss, valuess in values.items():
#                 if keyss == "city":
#                     city = valuess
#                     # address[valuess] = None
#                     # print(valuess)
#         if keys == "name":
#             name = values
#     address.setdefault(city, []).append(name)
# # print(address)

# Более красивый и короткий:
for user in users:
    city = user["address"]["city"]
    name = user["name"]
    address.setdefault(city, []).append(name)
# print(address)

with open("cities.json", "w") as f:
    json.dump(address, f, indent=4)
