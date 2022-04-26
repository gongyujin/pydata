data='aaa,bbb,ccc'
data_02='aaa bbb ccc'
data_03='aaa   bbb   ccc'
data2=data.split(',')
print(data2)
print(type(data2))

data3=data_02.split(' ')
print(data3)

data4=data_03.split('\t')
print(data4)