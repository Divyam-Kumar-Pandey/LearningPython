s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2)) # this doesn't changes s1
s1.update(s2) # this changes s1
print(s1.intersection(s2)) # this will not update s1
s1.intersection_update(s2) # this will update s1
s3 = s1.symmetric_difference(s2) # AuniB - AintB 

s3 = s1.difference(s2) # A - AintB
s1.difference_update(s2) # this will update s1
print(s3) 
print(s1, s2)

print(s1.isdisjoint(s2))

cities = {"Kolkata", "Delhi", "Mumbai"}
cities.add("Chennai")
print(cities)
cities.update({"A", "B"})
print(cities)

cities.remove("A") # throws error if not present
cities.discard("A") # does the same, but doesn't throws error

cities.pop() # used to remove any one element from the set
# del cities # deletes the set
# if we don't want to delete the set, just delete all of its elements
# cities.clear()