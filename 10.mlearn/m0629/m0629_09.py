data=[1.5,1.9,3.5,4.8,5.9]

# 함수호출 1
# lambda 함수호출, lambda a에서 a는 매개변수를 의미, int(a): 실행문
# map_data=list(map(lambda a : int(a),data))  ==> lambda a : int(a) 는 func

# 함수호출 2
# lambda는 func을 의미 int(a)는 return된 것을 의미
def func(a): 
    return int(a)
map_data=list(map(func,data))

print('data : ',data)
print("map데이터 결과값 : ",map_data)
