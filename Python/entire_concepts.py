# data = [10, 20, 30, 40, 50]

# first, *middle, last = data

# print(first)
# print(middle)
# print(last)

# # Output
# # 10
# # [20,30,40]
# # 50


# tuple = 10  # this is not tuple because of only 1 value it will return int
# tuple = (10,)  # this is tuple when we put , when 1 values exists

# numbers = (10, 20, 10, 30, 10)

# print(numbers.count(50))

# print(data.count(10))


# data = ("A", "B", "A", "C", "A")

# print(data.count("A"))
# print(data.index("C"))
# print("B" in data)
# print(data + ("D",))


# This:

# data = {}

# creates an empty dictionary, not an empty set.

# For an empty set:

# data = set()

# remove(value)   → error if missing
# discard(value)  → safely does nothing if missing

data = {10, 20, 20, 30, 30, 30}

print(data)
print(len(data))
print(20 in data)
print(99 in data)

# {10,20,30}
# 3
# True
# False


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Predict these four:

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

# {1, 2, 3, 4 ,5 ,6}
# {3, 4}
# {1, 2}
# {1, 2, 5, 6}

person = {"name": "Alice", "age": 25, "country": "India"}

print(person["name"])
print(person["age"])
print("country" in person)

# Alice
# 25
# True

data = {"name": "Alice", "age": 25, "city": "Hyderabad"}

for key in data:
    print(key)

for value in data.values():
    print(value)

# name
# age
# city
# Alice
# 25
# Hyderabad

customer = {
    "id": 101,
    "name": "Alice",
    "address": {"city": "Hyderabad", "country": "India"},
}

print(customer["name"])
print(customer["address"]["city"])
print(customer["address"]["country"])

# Alice
# Hyderabad
# India

order = {"id": 5001, "customer": {"name": "Alice"}}

print(order.get("customer", {}).get("address", {}).get("city", "not found"))


import copy

original = {"customer": {"name": "Alice", "age": 25}}

new_data = copy.deepcopy(original)

new_data["customer"]["age"] = 40

print(original["customer"]["age"])
print(new_data["customer"]["age"])

#
numbers = [1, 2, 3, 4, 5]

result = {n: n * 10 for n in numbers if n > 2}

print(result)

# {3: 30, 4: 40, 5: 50}

name = "Alice"

print(hash(name))

#

data = [("Alice", 25), ("Bob", 30), ("Alice", 25), ("Charlie", 35)]

unique = set(data)

result = {name: age for name, age in unique}

print(len(data))
print(len(unique))
print(result)

# 4
# 3
# {alice: 25, bob:30, charlie:35}

print(2 % 2 == 0)

print(bool(""))
print(bool("Alice"))
print(bool([]))
print(bool([1, 2]))
print(bool(0))
print(bool(10))

# False
# True
# False
# True
# False
# True
