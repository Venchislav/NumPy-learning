import matplotlib.pyplot as plt


x = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
y = [2000, 4000, 3000, 1000, 7000]

plt.bar(x, y, label='profit')
plt.plot(x, y, color='green', marker='o', markersize=7)

plt.xlabel('Month')
plt.ylabel('profit')
plt.title('STONKS')
plt.legend()
plt.show()
