
list = [1,5,6,3,7]
result = list[::]
print(result)
print(list[1:])
print(list[::-1])
print(list[0:100])

mixed_dict = {"tom":123,456:741}
print(mixed_dict["tom"])

dict2 = dict(zip(range(3),["apple","banana","grape"]))
print(dict2)
dict1 = {132:45}
print(dict1)
dict3 = dict(name=456)
print(dict3)

for ele in dict2 :
    print(dict2[ele])

for key,element in dict2.items():
    print(key,element)

a={3,5}
print(a)
print(type(a))

s={1,2,3}
s.add(3)
print(s)
