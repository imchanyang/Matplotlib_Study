import matplotlib.pyplot as plt
import numpy as np
# 선 그래프 그리기1 : y=x^2
x = np.arange(-9, 10)
y = x**2
# linestyle은 -, :, -., -- 등 사용
plt.plot(x, y, linestyle="-.", marker="*")
plt.show()

# 선 그래프 그리기2 : legend
x = np.arange(-9, 10)
y1 = x**2
y2 = -x

plt.plot(x, y1, linestyle="-.", marker="*", color="red", label="y = x^2")
plt.plot(x, y2, linestyle=":", marker="o", color="blue", label="y = -x")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(
    shadow=True,
    borderpad=1,
    loc="upper right"
)
plt.show()