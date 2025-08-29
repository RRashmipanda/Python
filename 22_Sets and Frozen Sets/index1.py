x = {"a","b","c"}

"a" in x
# True
'g' in x
# False

for i in x:
    print(i)
    # its print as b c a because set is unordered collection    

y = {"a","g","h"}
print(x|y) # union
print(x&y) # intersection
print(x-y) # difference
print(x^y) # symmetric difference
print(x<y) # subset

z = {"g","h"}
print(z<y)