

list1=[]
for x in range(10) :
    list1.append(x**2)
print(list1)

list2 = [x*x for x in range(10)]
print(list2)

list3 = list(map(lambda x:x*x ,range(10)))
print(list3)

vector = [[1,2],[3,4],[5,6]]
result = [num for ele in vector for num in ele]
print(result)

#2.过滤不符合条件的元素
list4 = [-1,-2,3,4,5]
result2 = [i for i in list4 if i>0]
print(result2)

#3.列表推导中使用多个循环实现多序列元素任意的组合，并过滤元素
list5 = [(x,y) for x in [1,2,3] for y in [2,3,4] if x!= y]
print(list5)