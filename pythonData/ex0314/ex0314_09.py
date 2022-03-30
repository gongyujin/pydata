# 3의 배수를 제외하고
# 넘을때의 총합과 숫자를 출력하시오.

total, i = 0, 0

for i in range(1,100):
    if i % 3==0:
        continue
    else:
        total+=i
        print('{},{}'.format(i,total))
    if total > 100:
        break

print('합 : {}'.format(total))
print('100을 넘었을 때 숫자 :', i)
print('100을 넘기 전 숫자 :', i-1)