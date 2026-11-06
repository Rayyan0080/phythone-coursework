#what does this print?

fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:     # by item
    print(afruit, end=" ")

print()

#what does this print?

fruits = ["apple", "orange", "banana", "cherry"]

for position in range(len(fruits)):     # by index
    print(fruits[position], end=" ")


for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi ", name, "  Please come to my party on Saturday!")
