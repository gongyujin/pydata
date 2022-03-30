class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuname,kor,eng):
        Student.stuname+=1
        self.stuno=Student.stuno
        self.stuname=stuname
        self.kor=kor
        self.eng=eng
        self.total=kor+eng
        self.avg=self.total/2
        
    def __str__(self):
        stuprint='{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        return stuprint
    
    def __lt__(self,other):
        return self.total < other.total 
    
    def __eq__(self, stuname):
        return self.stuname==stuname
    
    def getKor(self):
        return self.kor
    
    def setKor(self,kor):
        if kor>= 0:
            self.kor=kor
            self.total=kor+self.eng
            self.avg=self.total/2 
        else:
            print('입력이 잘못되었습니다.')
                
    def getEng(self):
        return self.eng
    
    def setEng(self,eng):
        if eng >= 0:
            self.eng=eng
            self.total=eng+self.kor
            self.avg=self.total/2     
        else:
            print('입력이 잘못되었습니다.')