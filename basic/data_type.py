a_string = "like this"
a_num = 3
a_float = 3.12
a_boolean = False
a_none = None

# list
days_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_list)
print("Sun" in days_list)
print("Sat" not in days_list)
print(days_list[2])
print(len(days_list))
days_list.append("Sat")
print(days_list)
days_list.reverse()
print(days_list)

# tuple
days_tuple = ("Mon", "Tue", "Wed", "Thur", "Fri")
print("Fri" in days_tuple)
# can't change things

# dict
info = {"name": "Nico", "age": 29, "korean": True,
        "fav_food": ["kimchi", "sashimi"]}
print(info["age"])
info["age"] = 27
print(info)
