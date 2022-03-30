# 폴더: 팩키지
import stu
        
s1=stu.Student('홍길동', 100, 100)
s2=stu.Student('이순신', 100, 100)
s3=stu.Student('유관순', 100, 100)

print('{},{},{}'.format(s1.stuNo,s1.stuName,s1.stuTotal))
print(s2)
print(s3) # 클래스에 def __str__(self):가 없으면 주소값만 나옴