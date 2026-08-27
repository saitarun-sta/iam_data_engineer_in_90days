# Removing values in sets

Two common methods:

remove()
numbers = {10, 20, 30}

numbers.remove(20)

Result:

{10, 30}

But if the value doesn't exist:

numbers.remove(99)

→ KeyError

discard()
numbers = {10, 20, 30}

numbers.discard(99)

No error.

So:

remove(value)   → error if missing
discard(value)  → safely does nothing if missing

This distinction is useful when processing messy real-world data.

8. Set operations

Sets become really interesting when comparing groups.

Suppose:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
Union

Everything from both sets:

a | b

→

{1, 2, 3, 4, 5, 6}

Think:

A OR B

Intersection

Values present in both:

a & b

→

{3, 4}

Think:

A AND B

Difference

Values in a but not b:

a - b

→

{1, 2}

Reverse it:

b - a

→

{5, 6}

Difference is directional.

Symmetric difference

Values that are in one set or the other, but not both:

a ^ b

→

{1, 2, 5, 6}
Mental model

For:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

Think:

A ∪ B  → everything
A ∩ B  → common
A - B  → only A
B - A  → only B
A △ B  → not common

These operations are surprisingly useful in data engineering—for example, comparing IDs between two datasets to find missing, new, or overlapping records.

# dictonary:

person["city"]       → strict lookup → KeyError if missing
person.get("city")   → safe lookup → None if missing
person.get("city", "Unknown") → safe lookup with default

One more useful pattern

You can safely access an optional nested field with .get():

city = customer.get("address", {}).get("city")

If "address" is missing, {} is used, and then .get("city") returns None.


# Dictionary Copying

Good choice. We'll do copying first, then deletion.

The same shallow/deep-copy idea you learned with lists applies to dictionaries too.

1. Simple dictionary copy
original = {
    "name": "Alice",
    "age": 25
}

new_data = original.copy()

new_data["age"] = 30

print(original)
print(new_data)

Output:

{'name': 'Alice', 'age': 25}
{'name': 'Alice', 'age': 30}

Why?

copy() creates a new outer dictionary.

original ──► {"name": "Alice", "age": 25}

new_data ──► {"name": "Alice", "age": 30}

Changing a direct value doesn't affect the original.

2. But nested dictionaries are different

Consider:

original = {
    "name": "Alice",
    "address": {
        "city": "Hyderabad"
    }
}

new_data = original.copy()

new_data["address"]["city"] = "Delhi"

print(original)
print(new_data)

What might surprise you:

{'name': 'Alice', 'address': {'city': 'Delhi'}}
{'name': 'Alice', 'address': {'city': 'Delhi'}}

Why did original change?

Because .copy() made a shallow copy.

The outer dictionaries are separate, but the nested "address" dictionary is shared.

original ──► outer dict A
                 │
                 └──► address dict ◄──┐
                                      │
new_data ──► outer dict B ────────────┘

So:

new_data["address"]["city"] = "Delhi"

changes the shared nested dictionary.

3. deepcopy()

If we want the nested structure to be completely independent:

import copy

original = {
    "name": "Alice",
    "address": {
        "city": "Hyderabad"
    }
}

new_data = copy.deepcopy(original)

new_data["address"]["city"] = "Delhi"

print(original)
print(new_data)

Now:

{'name': 'Alice', 'address': {'city': 'Hyderabad'}}
{'name': 'Alice', 'address': {'city': 'Delhi'}}

The nested dictionary was copied too.

Mental model
original.copy()
    ↓
shallow copy
    ↓
outer dictionary copied
nested mutable objects may be shared
copy.deepcopy(original)
    ↓
deep copy
    ↓
nested mutable objects copied recursively