# 4개의 값을 입력받아
# 합을 구하고 입력한 값을 출력하시오.

arrs=[]
total=0
for i in range(4):
    a=int(input('{}번째 숫자를 입력하세요.>> '.format(i+1)))
    arrs.append(a)
    total+=a
 
# for arr in arrs:
#     total += arr
    
print('입력한 숫자 :', arrs)
print('합 :',total)