# Set is unordered collection of unique elements
s = set([1, 2, 3, 4, 5, 2, 3])
print(s)
s.add(6)
print(s)
s.remove(3)
print(s)
# can not use s[0] as set is unordered

# frozen set means you should not be able to change the content of set
fs = frozenset([1, 2, 3, 4, 5, 2, 3])
print(fs)
# fs.add(6) # will raise error as frozen set is immutable