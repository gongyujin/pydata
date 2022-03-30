# def 함수이름() 함수선언
# 매개변수 개수 : (매개변수1, 매개변수2) - 매개변수는 호출개수와 함수선언의 매개변수 개수가 같아야함
# 매개변수 기본값: 매개변수 data=10, 매개변수가 들어오지 않으면 기본값(디폴트값)으로 설정
# 예) v3=10
# 리턴형태 : return 개수는 상관없음 리턴변수는 2개이상일때 튜플타입, 없으면 생략가능
# 가변매개변수 : 매개변수가 개수를 가변적으로 사용함. 함수이름(*para)
# dic 가변매개변수 : dic타입으로 가변매개변수 사용가능. 함수 이름(**para)


def dic_func(**para): #dictionary 매개변수 (키와 value를 다 받기 때문)
    for k,v in para.items():
        print('k, v의 값 :',k,v)
    
    # for k in para.keys():
    #     print('k의 값 : ', k)
        
    # for v in para.values():
    #     print('v의 값 : ', v)  
    
    return


dic_func(트와이스=9, 소녀시대=7, 걸스데이=4, 블랙핑크=4)