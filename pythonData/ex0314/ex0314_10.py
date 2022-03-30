# for i in range(10,0,-1):
#     for j in range(9,0,-1):
#         print(' '*j, end='')   
#     print('*'*i)
    
    
# for i in range(10,0,-1):
#     print('*'*i)
    

# i=10
# while i>=0:
#     j=0
#     while j<=i:
#         print('*',end='')
#         j +=1
#     print()
#     i -=1
    
# i=10
# while i>=0:
#     j=0
#     while j<=i:
#         print(' ',end='')
#         j +=1
#     print('*'*(10-j))
#     i -=1

# i=10
# while i>=0:
#     print(' '*i, end='')
#     print('*'*(10-i))
#     i-=1

#왼쪽 삼각형
for i in range(1,11):
    print('*'*i)
print('')
    
#오른쪽 삼각형
for i in range(1,11):
    print(' '*(10-i)+'*'*i)
print('')
    
#역삼각형
for i in range(1,11):
    print('*'*(11-i)+' '*i)
print('')

#가운데 삼각형
for i in range(1,11):
    print(' '*(10-i)+'*'*(2*i-1))