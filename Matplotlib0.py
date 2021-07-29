# Matplotlib란?
# 다양한 데이터를 시각화 할 수 있도록 도와주는 라이브러리
# 간단한 데이터 분석에서부터 인공지능 모델의 시각화까지 활용도가 매우 높음

import matplotlib.pyplot as plt
import numpy as np
# 간단한 직선 그래프 그리기


x = [1, 2, 3]
y = [1, 2, 3]
plt.plot(x, y)
plt.title("My Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 그래프 저장하기1 : y=x 직선 그래프
x = [1, 2, 3]
y = [1, 2, 3]
plt.plot(x, y)
plt.title("My Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('picture.png')


# 그래프 저장하기2 : sin, cos 그래프
# PI*10 너비에 500개의 점을 균일하게 찍기
x = np.linspace(0, np.pi * 10, 500)

# 2개의 그래프가 들어가는 Figure 생성(행, 열)
fig, axes = plt.subplots(2, 1)
# 첫번째는 sin 그래프
axes[0].plot(x, np.sin(x))
# 두번째는 cos 그래프
axes[1].plot(x, np.cos(x))
fig.savefig("sin&cos.png")

