

list=[101,2,102]
for i in range(0, len(list)):
   if list[i]>=100:
       list[i]=list[i]*list[i]
list[1]=100
for i in list:
    print(i)
print(100 in list)
# print(len(list))
#################################
list2=[2,4]
list2.append('a')
for i in list2:
    print(i)

dic1={"a":1,"b":2,"c":'apple'}
print(dic1)
for ele in dic1:
    print(ele)
    print(dic1[ele])