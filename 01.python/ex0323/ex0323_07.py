# 리스트를 만들어주는 형태
# map(함수,리스트) #함수에 적용하여 리스트 형태로 돌려주는것

list1=[1,2,3,4,5]

# add10=lambda num:num+10

print(list(map(lambda num:num+10,list1))) # map까지만 하면 (11,12,13,14,15)라고 나옴
# map을 하나의 for문이라고 생각하면 됨
# map(add10,[1,2,3,4,5]) add10와 1이 계산되어서 저장되고, add10과 2가 계산되어서 저장되는 방식