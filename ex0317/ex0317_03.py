# print(10+5)
# print(10-5)
# print(10*5)
# print(10/5)

def cal(a,b): #a,b : 매개변수
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
# return은 있을수도 있고 없을 수도 있음





a=10
b=5
cal(a,b) # a,b는 함수에 맞게 알아서 치환하기 때문에 함수에 써져있는것과 동일하게 쓸필요없이 원하는 매개변수를 입력하면 됨

cal(20,2)
cal(22,5)
cal(30,40)
cal(50,5)





# # def: 함수선언 --> 반복적인 작업 축약
# def singer(name, member, debut, song): 
#     return {'이름': name, '구성원': member,'데뷔':debut,'대표곡':song}


# singerList=[]
# singerList.append(singer('BTS',7,'2 cool 4 skool','Dynamite'))
# singerList.append(singer('블랙핑크',4,'square one','How you like that'))

# print(singerList)