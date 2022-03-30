#구구단
# 2*1=2
# 2*2=4
# 2*3=6

for i in range(2,9):
    if i%2==0:
        print('-'*30)
        print('{} 단'.format(i))
        print('-'*30)
        for j in range(1,10):
            if j%2==1:
                print('{} * {} = {}'.format(i,j,i*j))   
                
for i in range(2,9):
    
    print('-'*30)
    print('{} 단'.format(i))
    print('-'*30)
    for j in range(1,10):
        if j%2==1:
            print('{} * {} = {}'.format(i,j,i*j))   