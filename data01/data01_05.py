# 데이터 시각화 툴 matplotlib
from cProfile import label
from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

t = np.arange(0, 12, 0.01)  # 0.01 간격으로 0~12 데이터 만들기
y = np.sin(t)   # 데이터 sin에 삽입

plt.figure(figsize=(10,6))  # 그래프의 크기
plt.plot(t, y, lw=3, label='sin')
plt.plot(t, np.cos(t), color='red', label='cos')
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('sinewave')
plt.legend()    # 범례 추가
plt.show()