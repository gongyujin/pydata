class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    #제일먼저 들어감 (생성자)
    def __init__(self, stuname='',kor=0,eng=0): #디폴트값만들기
        Student.stuno+=1
        self.stuno=Student.stuno
        self.stuname=stuname
        # self.__kor=kor # private변수선언: __를 넣게 되면 더이상 외부에서 접근이 안됨(같은 클래스 내에서만 입력가능)
        self.kor=kor 
        self.eng=eng
        self.total=kor+eng
        self.avg=self.total/2
    
    def __str__(self): # 출력
        stuprint='{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint
    
    # 객체 작은지 비교
    def __lt__(self, other):
        return self.total < other.total
    
    # 객체 같은지 비교 (이름)
    def __eq__(self, stuname):
        return self.stuname==stuname
    
    def getKor(self):
        return self.kor    
        
    def setKor(self,kor):
        if kor >=0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg=self.total/2
        else:
            print('입력이 잘못되었습니다.')
            
            # try:
            #     raise Exception('입력이 잘못됨.') # 프로그램이 종료가 되지 않게 try, except를 넣어줘야함
            # except:
            #     pass
            
    def getEng(self):
        return self.eng    
        
    def setEng(self,eng):
        if eng >=0:
            self.eng=eng
            self.total=self.kor+eng
            self.avg=self.total/2
        else:
            print('입력이 잘못되었습니다.')
            
            # try:
            #     raise Exception('입력이 잘못됨.') # 프로그램이 종료가 되지 않게 try, except를 넣어줘야함
            # except:
            #     pass