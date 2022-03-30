class Car:
    color='white' # 기본속성
    tire=4
    speed=50
    def upSpeed(self, speed):
        self.speed=speed
        print('현재속도 :',self .speed)
        
        
class Sedan(Car): # 클래스 car를 다 가져오게됨 ; 상속
    # speed=10 # 정의를 새롭게 해줄 수 있음
    # def upSpeed(self, speed):
    #     self.speed=speed*2
    #     print('현재속도 :',self .speed)
    pass


class Trunk(Car):
    pass


c1=Sedan()
print(c1.speed)