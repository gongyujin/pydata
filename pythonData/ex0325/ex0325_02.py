class Graphic2d: # 클래스는 함수가 들어가 있는 데이터 저장공간
    x=0
    y=0
    
    # 그래픽을 보여주는 로직--> 100만줄
    # 수정 로직 10만줄

    def gprint(self):
        return '{},{}'.format(self.x,self.y)
        

class Graphic3d(Graphic2d): # super쓰려면 클래스 괄호에 전클래스 이름 써줘야함
    z=0 # x,y는 필요없음: 2d를 그대로 들고 왔기 때문
    
    def gprint(self): # 재정의 하는 것: 오버라이딩
        # return '{},{},{}'.format(self.x,self.y,self.z)
        return '{},{}'.format(super().gprint(),self.z) #super을 사용해서 이전 return을 그대로 쓸 수 있음
        
        
g1=Graphic2d()
print(g1.gprint())

g2=Graphic3d()
print(g2.gprint())