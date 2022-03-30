list_names=['주바다','공유진','김샛별','송선유','양홍욱']

for i, list_name in enumerate(list_names): #인덱스번호를 뽑아줄 수 있음, 번호를 해주고 싶을 때 enumerate사용하면 됨
    print('{}. {}'.format(i+1, list_name))

# count=1
# for list_name in list_names:
#     print('{}.'.format(count),list_name)
#     count+=1