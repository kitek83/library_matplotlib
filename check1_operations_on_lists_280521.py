list = [1,2,3,4,5] * 2
print(list)
list2 = [10,20,30,40]
list3 = list2
print(list3)
print('------------------------')
list4 = ['Marek','Jacek','Darek','Olek']
list4[0] = 'Adam'
print(list4)
list4.insert(0,'Patryk')
print(list4)
list4.append('Alex')
print(list4)
print('##########################')
list4.remove('Jacek')
print(list4)
del list4[0]
print(list4)