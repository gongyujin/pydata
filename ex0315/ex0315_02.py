list1=['주바다','공유진','김샛별','송선유','양홍욱','윤상운','이한구']

while True:
    search = input('이름을 입력하세요.>> ')
    if search in list1:
        print('출석했습니다.')
    else:
        print('출석 전 입니다.')


# list1=[i for i in range(0,10)] # list1은 list타입
# print('list1 타입', type(list1))

# for i in range(0,10):
#     print(i) # i는 int형이 됨
#     print('i 타입', type(i))
    
# list1=['주바다','공유진','김샛별','송선유','양홍욱']

# for idx,i in enumerate(list1):
#     print('{}. {}'.format(idx+1,i))
    
# idx=1  
# for i in list1:
#     print('{}. {}'.format(idx,i))
#     idx+=1  

# for i in range(len(list1)):
    # print('{}. {}'.format(i+1,list1[i]))

# # 2 * 1 = 2 : 1번째 for문은 단부분에 해당됨
# for p in range(2,10):
#     print('[ {:4d}단  ]'.format(p),end=' ')
# print()

# for i in range(1,10):
#     for j in range(2,10):
#         print('{} X {} = {:2d}'.format(j,i, i*j),end='  ')
#     print()    
        
