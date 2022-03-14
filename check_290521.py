list1 = ['Darek', 'Krysiek','Daniel','Maciek','Michael']
list2 = [] + list1
print(list2)
list3=[]
for name in list1:
    list3.append(name)
print(list3)
print('----------------------')
del list3[0]
print(list3)
list3.remove('Michael')
print(list3)
print('#################################')
nums = [1,2,3,4,5,6]
b = min(nums)
print(b)
