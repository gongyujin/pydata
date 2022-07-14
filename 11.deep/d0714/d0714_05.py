from tensorflow import keras
import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# mnist파일 불러오기
# keras mnist파일이 설치될때 자동설치가 됨
# 튜플형태로 자동적으로 가져오게 됨
(train_data,train_label),(test_data,test_label)=keras.datasets.fashion_mnist.load_data()

train_scaled=train_data/255.0
test_scaled=test_data/255.0
