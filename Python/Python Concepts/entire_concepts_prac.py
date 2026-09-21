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

# data = {10, 20, 20, 30, 30, 30}

# print(data)
# print(len(data))
# print(20 in data)
# print(99 in data)

# # {10,20,30}
# # 3
# # True
# # False


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# # Predict these four:

# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)

# # {1, 2, 3, 4 ,5 ,6}
# # {3, 4}
# # {1, 2}
# # {1, 2, 5, 6}

# person = {"name": "Alice", "age": 25, "country": "India"}

# print(person["name"])
# print(person["age"])
# print("country" in person)

# # Alice
# # 25
# # True

# data = {"name": "Alice", "age": 25, "city": "Hyderabad"}

# for key in data:
#     print(key)

# for value in data.values():
#     print(value)

# # name
# # age
# # city
# # Alice
# # 25
# # Hyderabad

# customer = {
#     "id": 101,
#     "name": "Alice",
#     "address": {"city": "Hyderabad", "country": "India"},
# }

# print(customer["name"])
# print(customer["address"]["city"])
# print(customer["address"]["country"])

# # Alice
# # Hyderabad
# # India

# order = {"id": 5001, "customer": {"name": "Alice"}}

# print(order.get("customer", {}).get("address", {}).get("city", "not found"))


# import copy

# original = {"customer": {"name": "Alice", "age": 25}}

# new_data = copy.deepcopy(original)

# new_data["customer"]["age"] = 40

# print(original["customer"]["age"])
# print(new_data["customer"]["age"])

# #
# numbers = [1, 2, 3, 4, 5]

# result = {n: n * 10 for n in numbers if n > 2}

# print(result)

# # {3: 30, 4: 40, 5: 50}

# name = "Alice"

# print(hash(name))

# #

# data = [("Alice", 25), ("Bob", 30), ("Alice", 25), ("Charlie", 35)]

# unique = set(data)

# result = {name: age for name, age in unique}

# print(len(data))
# print(len(unique))
# print(result)

# # 4
# # 3
# # {alice: 25, bob:30, charlie:35}

# print(2 % 2 == 0)

# print(bool(""))
# print(bool("Alice"))
# print(bool([]))
# print(bool([1, 2]))
# print(bool(0))
# print(bool(10))

# # False
# # True
# # False
# # True
# # False
# # True

# print([100] + [200])


# def add_value(data):
#     # data = data + [100]
#     return data


# numbers = [10, 20, 30]


# result = add_value(numbers)

# print(numbers)
# print(list(range(1, 3)))

# import csv

# customers = [
#     ["name", "age", "country"],
#     ["Alice", "25", "India"],
#     ["Bob", "30", "USA"],
# ]

# with open("customers.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerows(customers)


def parse_age(value):
    try:
        # conversion
        converted_value = int(value)

        # validation
        if 0 <= converted_value <= 120:
            return converted_value, None

        return None, "invalid age"

    except (ValueError, TypeError):
        return None, "invalid age"


# valid_customers = []
# invalid_customers = []

# if age is not None:
#     # process valid record
#     valid_customers.append({row["name"], age, row["country"]})
#     # print(f"VALID: {row["name"]}")
# else:
#     # log/quarantine invalid record
#     valid_customers.append({row["name"], row["age"], row["country"]})

# print(f"INVALID: {row["name"]}, age={row["age"]}")


# if age is not None:
#     # process valid record
#     valid_customers.append({"name": row["name"], "age": age, "country": row["country"]})
# else:
#     # log/quarantine invalid record
#     invalid_customers.append(
#         {"name": row["name"], "age": row["age"], "country": row["country"]}
#     )

# clean_row = row.copy()

# clean_row["age"] = age

# x = [10, 20, 30, 40, 50]

# print(x[4:1:-1])
# print(x[1:4:-1])
# print(x[1:4:1])
# print(x[-1:-4:-1])


# def total(*numbers):
#     print(type(numbers))
#     return sum(numbers)


# print(total(1, 2, 3))
# print(total(10, 20))
# print()

# rows = [
#     {"name": "Rahul", "age": "25", "country": "India"},
#     {"name": "", "age": "30", "country": "India"},
#     {"name": "Priya", "age": "150", "country": ""},
#     {"name": "Amit", "age": "abc", "country": "India"},
#     {"name": "Sara", "age": "28", "country": "USA"},
# ]

valid_customers = []
invalid_customers = []
# total_rows = 0
# valid_rows = 0
# invalid_rows = 0

# for row in rows:
#     # write your code here
#     errors = []

#     if not row["name"].strip():
#         errors.append("missing name")

#     age, age_error = parse_age(row["age"])

#     if age_error is not None:
#         errors.append(age_error)

#     if not row["country"].strip():
#         errors.append("missing country")

#     if errors:
#         rejected_row = row.copy()
#         rejected_row["errors"] = errors
#         invalid_customers.append(rejected_row)
#         invalid_rows += 1
#     else:
#         approved_row = row.copy()
#         approved_row["age"] = age
#         valid_customers.append(approved_row)
#         valid_rows += 1

#     total_rows += 1

# import csv

# # Write valid customers
# with open("valid_customers.csv", "w", newline="") as file:

#     writer = csv.DictWriter(file, fieldnames=["name", "age", "country"])

#     # write header
#     writer.writeheader()

#     # write rows
#     writer.writerows(valid_customers)


# rejected_row_copy = copy.copy(rejected_row)

# converted_errors = ";".join(rejected_row["errors"])

# # put converted_errors into the copy
# rejected_row_copy["errors"] = converted_errors

# # add the copy to rejected_rows_for_csv
# rejected_rows_for_csv.append(rejected_row_copy)


def validate_row(row):
    errors = []

    if "name" in row:
        # your code here
        if row["name"].strip():
            pass
        else:
            errors.append("missing name")
    else:
        # your code here
        errors.append("missing name column")

    if "age" in row:
        age, age_error = parse_age(row["age"])
        if age is not None:
            pass
        else:
            errors.append(age_error)
    else:
        errors.append("missing age column")

    if "country" in row:
        # check the value
        if row["country"].strip():
            pass
        else:
            errors.append("missing country")
    else:
        # missing column
        errors.append("missing country column")

    return errors


# DECIDE WHETHER ROW IS VALID OR INVALID

# if there are errors:
# if errors:
# #     create rejected row
#     rejected_row = row.copy()
# #     preserve original row
# #     add errors
#     rejected_row["errors"] = errors
# #     append to invalid_customers
#     invalid_customers.append(rejected_row)
# #
# # otherwise:
# else:
# #     create approved row
#     approved_row = row.copy()
# #     use approved_name, approved_age, approved_country
#     approved_row["name"] = approved_name
#     approved_row["age"] = approved_age
#     approved_row["country"] = approved_country
# #     append to valid_customers
#     valid_customers.append(approved_row)

# row = {"name": "Rahul", "age": "25", "country": "India"}
# row = {
#     "name": "Amit",
#     "age": "abc",
#     "country": "India"
# }
row = {"name": "Amit", "age": "abc", "country": "India"}


print(validate_row(row))
