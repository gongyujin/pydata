import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=10
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df=pd.read_excel('score.xlsx')
# print(df.groupby('학교').get_group('구로고'))
# int, float 평균을 계산해서 보여줌
# print(df.groupby('학교').mean())
print(df.groupby('학교')['키'].mean())
print(df.groupby('학교')['키'].mean().shape)
print(df.groupby('학교')['국어'].sum())
print(df.groupby('학교')['국어'].count())