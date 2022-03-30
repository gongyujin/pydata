aa=[]
bb=[]

for i in range(200):
    aa.append(i*3)
    
for j in range(200):
    bb.append(aa[199-j])

print(aa[3:9]) #3부터 8까지 출력
print(aa[:32]) #처음부터 31까지 출력
print(aa[100:]) #100부터 끝까지 출력
print(aa[190:210]) #index가 없는 것을 출력하면 있는 것까지만 출력 ==> 오류나지 않음
print(aa[-7:]) #맨뒤부터 -7까지 출력
print(aa[190:-5]) #뒤에서 5번째부터 190까지 출력 

# # aa list 100개: 0,2,4,8...
# aa=[]
# bb=[]

# for i in range(100):
#     aa.append(i*2)
    
# for j in range(100): #0,1,2,3,4.... ==> 99,98,97,...
#     bb.append(aa[99-j])
    