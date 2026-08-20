data = {
    "name": "Sai Tarun",
    "age": 26,
    "roll_no": 1,
    "marks": 98,
}

data["marks"] = 99

# other ways to update
data.update({"marks": 100})

data |= {"marks": 101}

# for nested dictionaries
# student["marks"]["math"] = 95

print(data)

# Deleting the data

# del student["city"] Deletes a key-value pair.
# pop() Deletes a key and returns its value.
# popitem() Removes the last inserted key-value pair and returns its value.
# clear() Removes all items from the dictonary.
