#!/usr/bin/python

#g1
#get unique elements
nums = [0.34, 0.55, 0.62, 0.63, 0.55, 0.34, 0.34, 0.45]
nSet = set(nums)
print(nums)
print(nSet)
#nSet.sort()
#print(nSet[1])
#unique = list(nSet)
#unique.sort()
#print(unique)

'''
#g2

aSet = {'ruby', 'sapphire', 'jade', 'emerald', 'diamond', 'amethyst', 'tourmaline'}
bSet = {'sapphire', 'diamond', 'agate', 'garnet', 'jade'}

#set operations
print("Set Operations")
print(aSet)
print(bSet)
union = aSet | bSet
print("a | b : "+str(union))
intersection = aSet & bSet
print("a & b : "+str(intersection))
subset = aSet < bSet
print("a < b : "+str(subset))
superset = aSet > bSet
print("a > b : "+str(superset))
difference = aSet - bSet
print("a - b : "+str(difference))
symmDifference = aSet ^ bSet
print("a ^ b : "+str(symmDifference))


print("\n----------\n")


#set methods
print("Set Methods")
cSet = {'June', 'September', 'October', 'May', 'July', 'April'}
dSet = {'June', 'May', 'August', 'December'}
print(cSet)
print(dSet)
eUn = cSet.union(dSet)
print("c.union(d) : "+str(eUn))
eSet = cSet.intersection(dSet)
print("c.intersection(d) : "+str(eSet))
eSub = eSet.issubset(cSet)
print("e.issubset(c) : "+str(eSub))
dSuper = dSet.issuperset(eSet)
print("d.issuperset(e) : "+str(dSuper))
cDiff = cSet.difference(eSet)
print("c.difference(e) : "+str(cDiff))
sDiff = dSet.symmetric_difference(cSet)
print("d.symmetric_difference(c) : "+str(sDiff))
'''
