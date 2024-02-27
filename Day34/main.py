ep1 = {
    121 : 45,
    324 : 78,
    432 : 89,
    987 : 65   
}

ep2 = {
    809 : 86,
    708 : 76,
    970 : 71
}

# set are unordered and unindexed, whereas dictionary are ordered and indexed

# ep1.update(ep2) # add ep2 to ep1
ep1.clear() 
ep1.pop(324) # remove 324 from ep1
ep1.popitem() # remove the last item from ep1
# del ep1[432] # remove 432 from ep1
# del ep1 # delete ep1
print(ep1)