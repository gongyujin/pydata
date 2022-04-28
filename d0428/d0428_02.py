import pandas as pd

temp = pd.Series([-20,-10,10,20],index=['Jan','Feb','Mar','Apr']) # 인덱싱을 해줄 수 있음

# print(temp[0]) # index 번호로 출력
print(temp['Jan']) # index 이름으로 출력
