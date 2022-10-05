mountains = ['Mount Kilimanjaro', 'Mount Kenya', 'Mount Stanley', 'Mount Meru']
print(mountains)
print(['Mount Kilimanjaro', 'Mount Kenya', 'Mount Stanley', 'Mount Meru'])
len(mountains)
print(len(mountains))
sorted(mountains)
print(mountains)
# The sorted function makes a temporary change.
print(sorted(mountains, reverse=True))
print(mountains)
# The methods append and insert make a permanent change.
# Lists are mutable.
mountains.append('Mount Meru')
print(mountains)
mountains.insert(-2, 'Mount Speke')
print(mountains)
del mountains[-3]
print(mountains)
mountains.remove('Mount Meru')
print(mountains)
print(f"Let's pop this element off the list: {mountains.pop()}.")
print(mountains)
print(f"The tallest mountain in Africa is: {mountains.pop(0)}.")
print(mountains)
# You can index in strings, as well as lists.
print("Dominic"[0])
print(len("Dominic"))
mountains.reverse()
print(mountains)
name = "Dominic"
name.lower()
# The name has not changed. Strings are not mutable.
print(name)
print(name.lower())
print(name)
print(mountains)
mountains.sort()
print(mountains)
mountains.insert(0, 'Mount Kilimanjaro')
print(mountains)
mountains.append('Mount Meru')
print(mountains)
heights = [5895, 5199, 5109, 4562]
for height in heights:
    print(height)
print()
for i in range(4):
    print(heights[i])
print()
for i in range(len(heights)):
    print(heights[i])
print()
facts = []
for i in range(len(mountains)):
    facts.append(f'The height of {mountains[i]} is {heights[i]} m.')
print(facts)

mountains[3] = 'Mount Speke'
print(mountains)

print(heights)
print(min(heights))
print(max(heights))
# The total height is not meaningful.
print(sum(heights))


