# 구구단

i=1
while i<=9:
    if i%3!=0:
        print('2 * {} = {}'.format(i,2*i))
    i+=1
    

i=1
while i<=9:
    if i%3==0:
        i+=1
        continue #break: 반복문 완전빠져나옴, continue 1번만 빠져나옴
    
    print('2 * {} = {}'.format(i,2*i))
    
    i+=1


# 1-100 홀수만 출력하시오.

# ch=1

# while ch<=100:
#     if ch%2==1:
#         print(ch)
    
#     ch +=1
 
    
# ch=1
# while ch<=100:
#     if ch%2==1:
#         print(ch)
#         ch +=1    
#     else:
#         ch +=1