import pandas as pd

df=pd.read_excel('user.xlsx',index_col='id')

df['total']=0
print(df)

# 500,505,910,950
# 601:700
df['total'][500,505,910,950]=100
df['total'][601:700]=100
print(df)