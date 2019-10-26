

set1 = set({1,2,3})
set2 = {3,4,5}
result = set1 | set2
print(result)
print(set1.union(set2))

print(set1 & set2)
print(type(set1.intersection(set2)))


print(set1<set2)

set3 = {3}
print(set3<set1)
print(set1>set3)
print(list((1,2)))

print (list(range(1,10,2)) )#将range对象转化为列表

print(list({'a':3,'b':9,'c':78}.items()))#将字典的”键“转化为列表
