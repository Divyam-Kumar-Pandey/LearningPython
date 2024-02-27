list = [5, 8, 3, 6, 1, 2]
print(list)
list.append(-1)
print(list)
# list.sort()
list.sort(reverse=True)
# or we can use 
# list.reverse()
print(list)
print(list.index(1)) # returns the index where 1 is present
print(list.count(5)) # returns the count of 5

# m = list
# m[0] = 0 # this will also reflect the change in original 'list'
m = list.copy()
# now the changes in m, will not reflect in 'list'
list.insert(2, 7) # 7 will inserted at index 2
print(list)

colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

k = list + m
print(k)