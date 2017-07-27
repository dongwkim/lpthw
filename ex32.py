the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oragne', 'pears', 'apricots']
change = [1, 'pennies', 2,'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

elements2D = [ [1,2,3],[4,5,6]]
# for i in range(0, elements2D.count()):
print(elements2D.count([2,2,3]))
