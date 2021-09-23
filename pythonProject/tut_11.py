# "SETS IN PYTHON"
# Set return unique values


s=set()
#print(type(s))
#l=[1,3,5,7,9,11]
#s_from_list=set(l)
#print(s_from_list)
s.add(1)
s.add(2)
print(s)
s=s.union({7,8,9})
print(s)
s=s.intersection({2,8})
print(s)
s1={3,4,5}
print(s.isdisjoint(s1))
