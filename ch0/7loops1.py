name = "Alice"
print(f"name is {name} {type(name)}")
for char in name:
    print(f" char is {char} {ord(char)}")

coordinates = (10.0, 20.0)
print(f"\ncoordinates is {coordinates} {type(coordinates)}")
for num in coordinates:
    print(num)

names = ["Alice", "Bob", "Charlie"]
print(f"\nnames is {names} {type(names)}")
for name in names:
    print(name)
    for char in name:
        print(f" char is {char} {ord(char)}")
