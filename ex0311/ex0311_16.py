# 1-25까지 list만들어보세요.
# [
# [1,2,3,4,5],
# [6,7,8,9,10]    
#   ]
arrs=[i for i in range(1,26)]
arrs2=[[],[],[],[],[]] #2차원 리스트 생성 => 나중에는 딕셔너리 형태로 씀 ; [{},{},{}]

#arrs=[1,2,3,4,5,....]
# #i=0,1,2,3,4,5,6,....
for i,arr in enumerate(arrs):

    # arrs2[0].append(1,2,3,4,5)
    # arrs2[1].append(6,7,8,9,10)
    # arrs2[2].append(11,12,13,14,15)
    
    # i: 0,1,2,3,4 ->0, 5,6,7,8,9->1
    arrs2[i//5].append(arr)
    
print(arrs2)
print("[0][0] 데이터 :",arrs2[0][0])
print("[1][0] 데이터 :",arrs2[1][0])
print("[2][2] 데이터 :",arrs2[2][2])

# arr_list=[]
# count1=0
# for i in range(0,5):
#     num_list=[]
#     for j in range(5):
#         count1+=1
#         num_list.append(count1)
    
#     arr_list.append(num_list)

    
# print(arr_list)