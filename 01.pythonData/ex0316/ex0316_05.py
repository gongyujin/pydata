# from ast import operator
import operator

tdic,tlist={},[]

tdic={'love':'사랑','chair':'의자','game':'게임','car':'자동차'}

# items(): key와 value를 튜플형태로 출력: list 형태로 출력
tlist2=list(tdic.items())
tlist2.sort(reverse=True) #list로 변환된 것을 sort시켜줌
print(tlist2)

tlist=sorted(tdic.items(), key=operator.itemgetter(1)) #1은 value정렬,-1은 key의 역순정렬
print(tlist)


# print(tdic.keys())
# print(tdic.values())
# print(list(tdic.keys()))


# tlist=[4,6,1,8,9,11,2]
# # 기존 list는 변경되지 않음
# tlist2=sorted(tlist) # 기존 원본데이터를 유지해야할 때 사용
# print(tlist2)
# print(tlist)

# # tlist.sort(reverse=True)
# # print(tlist)

# tlist.reverse() #입력값 역순
# print(tlist)
