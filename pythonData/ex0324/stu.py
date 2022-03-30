class Student:
    stuNo=0
    stuName=''
    stuKor=0
    stuEng=0
    stuTotal=0
    stuAvg=0
    stuRank=0
    
    # 클래스 생성시 최초 1회 생성
    def __init__(self,stuName,stuKor,stuEng):
        Student.stuNo +=1 # 전역변수라고 봐도 됨
        self.stuNo =Student.stuNo # 클래스변수에서 1증가해서 자동입력 (따로 입력해줄필요 없음)
        self.stuName=stuName
        self.stuKor=stuKor
        self.stuEng=stuEng
        self.stuTotal=stuKor+stuEng
        self.stuAvg=(stuKor+stuEng)/2
        
    # # 객체를 호출시 자동으로 함수 실행, 이 함수가 없으면 저장되어 있는 주소만 보여줌
    def __str__(self):
        return '{},{},{},{}'.format(self.stuNo,self.stuName,self.stuKor,self.stuTotal)

    def setKor(self, stuKor): # s1=stu.Student('홍길동', 100, 100)에서 점수를 수정하고 싶을때 total도 같이 수정되어야함
        if stuKor >=0:
            self.stuKor=stuKor
            self.stuTotal = stuKor + self.stuEng
            self.stuAvg=self.stuTotal/2
        else:
            print('입력값이 잘못되었습니다.')
            
              
    # 실행하는 곳이 자신인지 확인
    if __name__ == '__main__':
        print('현재 자신에서 호출되어 실행함. 클래스 이름은 '+'Student')
    else:
        print('Student클래스가 호출 됨')