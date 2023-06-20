set1 = set()
set2 = set()
for i in range(1,6):
 set1.add(i)
for i in range(3,8):
 set2.add(i)
print("set1 =",set1)
print("set2 =",set2)
print("\n")
set3=set1|set2
print("Union of set1 & set2:set3=",set3)
set4 = set1 & set2
print("Intersection of set1 & set2:set4=",set4)
print("\n")
if set3 > set4:
 print("set3 is superset of set4")
elif set3 <_set4:
 print("set3 is superset of set4")
else:
 print("set3 is same as set4")
if set4 < set3:
 print("set4 is subset of set3")
 print("\n")
 set5 = set3-set4
print("Elements in set3 and not in set4:set5=",set5)
print("\n")
