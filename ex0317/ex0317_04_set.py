# # 리스트, 딕셔너리, 튜플, 세트(딕셔너리와 같은 형태, value없이 key 형태로만 이루어짐)
# # 1. set형태 - 중복을 제거

# myset={1,2,3,4,5,5}
# print(myset)

# # 2. 리스트를 set변경, set 다시 리스트로 변경
# # 리스트를 세트로 변경
# mylist=[9,12,1,2,4,4,5,5,1,2,6,7,8]
# myset=set(mylist) # 중복제거와 정렬이 자동으로 된다.
# print(myset)
# # 리스트로 타입변경
# mmylist=list(myset)
# print(mmylist)

# # 딕셔너리 추가
# mylist={'이름':'홍길동'}
# mylist['id']='aaa'
# print(mylist)

# # 3. set추가, 삭제
# myset ={1,2,3}
# myset.add(4) # 추가
# print(myset)
# myset.remove(2) # 삭제
# print(myset)
# myset.clear() # 모두삭제
# print(myset)

# # 4. set 2개를 합집합, 교집합, 차집합, 대칭차집합
# adic={1,2,3,4,5}
# bdic={3,4,5,6,7}
# print(adic | bdic) #합집합
# print(adic & bdic) #교집합
# print(adic - bdic) #차집합A
# print(bdic - adic) #차집합B
# print(adic ^ bdic) #대칭 차집합

# saleList=['삼각김밥','바나나','도시락','삼각김밥','도시락','오뎅','바나나']
# print(set(saleList)) # 리스트를 set하게 되면 자동적으로 중복이 삭제되면서 딕셔너리로 바뀌게 됨
# # 클래스는 "set"이지만 나타나는 것은 딕셔너리
# saledic=set(saleList) #중복이 제거되면 요소의 순서도 자동으로 변경됨 ex) {1,2,4,4,5,6}: 0,1,2,3,4,5 --> {1,2,4,5,6}: 0,1,2,3,4
# print(type(saledic))



# # 리스트를 합쳐서 결합시키면 개수가 다 합쳐지지만 세트를 결합시키면 중복을 제외하고 합쳐진다
# zipcode1={66012,66017,66075,66013,66019}
# zipcode2={66012,66017,66075,66015,66018}

# print(zipcode1|zipcode2) # 합집합 사용
# print(zipcode1-zipcode2)
# print(zipcode1^zipcode2) # 대칭 차집합: 차집합을 제외하고 모든 데이터

# numdic={1,2,33,3,3,5,1,9,2,3} # set은 키를 모아둔것인데 같은게 반복되면 같은 key가 중복이기때문에 덮어씌우기 됨
# numdic2={2,3,4,5,2,3,9,10,11}
# print(numdic) # 3이 중복이기때문에 엎어씌워짐
# print(numdic2)
# # print(numdic+numdic2) # type이 set이기 때문에 +를 사용할 수 없음
# print('numdic&numdic2 (교집합)', numdic&numdic2) # 교집합 (중복되는 것만 출력)
# print('numdic|numdic2 (합집합)', numdic|numdic2) # 합집합
# print('numdic - numdic2 (차집합)', numdic - numdic2) # 차집합
# print('numdic2 - numdic (차집합)', numdic2 - numdic) # 차집합


# adic={1:'aaa',2:'bbb',3:'ccc',1:'ddd'} # 같은 키값에 덮어씌우기됨
# print(adic)



# print(numdic)
# numdic2={4,5,2,9,10,30,20,7,8}

# nlist1=[1,2,5,4,8]
# nlist2=[3,4,5,8,2]

# print(nlist1+nlist2)

# print(numdic1)
# print(numdic2)


# tempdic1={1,2,33,3,3,5,1,9,2,3}
# numdic1=set(numdic1) # 중복된 것을 제외하고 재배열됨
# print(numdic1)


# tdic={'pig':'돼지','tiger':'호랑이','lion':'사자','dog':'개'}
# print(tdic)
# dtuple=list(tdic.items())
# dtuple.sort(reverse=True)
# print(dtuple)
# print(type(dtuple))
# tdic=dict(dtuple)
# print(type(tdic))
