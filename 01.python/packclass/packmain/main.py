import sys # 다른폴더에 있을때
# sys.path.append('/pydata/packclass') # 완전 다른 폴더 에 있으면 사용
# 상위폴더 안에 들어 있는 것이면 path.append를 하지 않아도 됨
from packsub2.school1 import Schseoul
# print(sys.path)
s1=Schseoul()
s1.schname()