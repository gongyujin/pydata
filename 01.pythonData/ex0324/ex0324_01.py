# 클래스의 이름 대문자, 벼수 소문자, 함수 소문자()
class Car:
    color="white" # 딕셔너리 구조가 포함되어 있다고 생각하면 됨
    speed=0
    
    def upSpeed(self,speed): # self는 car로 모든걸 받겠다는 의미
        self.speed += speed #value(speed) 로 속도 조절, self를 해주지 않으면 speed 변수 그대로 저장되기 때문에 class나오게 되면 사라지게 됨
        # global을 정하지 않고 self로 같은 의미로 만들어줌
    def downSpeed(self,speed):
        self.speed -= speed
        
a=Car() #인스턴스 생성
a.upSpeed(10)
print(a.speed)


# print(a.color)
# print(b.color)
# print('현재 속도 :', a.speed)
# a.upSpeed(10)
# print('현재 속도 :', a.speed)

# print('b의 속도 :', b.speed)


    
    
# car = Car()    # 넣어지게 되면 독립객체이기 때문에 마음대로 사용할 수 있음
# car2 = Car()
# car3 = Car()

# car4 = car # 주소를 복사한 것이기 때문에 이렇게 사용해서는 안됨

# a=1

# b=a
# c=a
# d=a
