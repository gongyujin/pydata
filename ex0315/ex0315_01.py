arr_list=[[1,2,3,4,5],[6,7],[8,9,10]]

for arr in arr_list:
    for i in arr:
        print(i)

# arr_list=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

# # 2차원 list는 for를 2번 돌려야 함.
# for arr in arr_list:
#     #arr: [1,2,3,4,5]
#     for i in arr:
#         print(i)


# arr_lists=[1,2,3,4,5,6,7]

# for arr_list in arr_lists:
#     print(arr_list)

# 2개의 입력한 숫자의 사이의 합을 출력하시오.
# 타입: bool-True/False, int-정수형, float-실수형, str-문자형
# 나누기-> int:float, 더하기 빼기, 곱하기 -> int

# input1=int(input('첫번째 숫자를 입력하시오.>> '))
# input2=int(input('두번째 숫자를 입력하시오.>> '))

# total=0
# for i in range(input1,input2+1):
#     total+=i
# print('{}부터 {}까지의 합 : {}'.format(input1,input2,total))

# total=0
# for i in range(101):
#     total+=i
    
# print('1부터 100까지의 합 :', total)