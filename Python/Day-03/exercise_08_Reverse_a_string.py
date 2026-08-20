# with reversed function

word = "saitarun"
reverse_string = ""

for char in reversed(word):
    reverse_string += char

print(reverse_string)

# with string slicing

# sequence[start:stop:step]
reversed_string = ""
for char in word[::-1]:
    reversed_string += char

print(reversed_string)