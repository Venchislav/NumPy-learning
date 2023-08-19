import matplotlib.pyplot as plt
import random


x = [random.randint(10, 100) for i in range(1000)]
y = [random.randint(10, 100) for i in range(1000)]

plt.scatter(x, y)
plt.title('nesquik')
plt.show()
