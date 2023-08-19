import matplotlib.pyplot as plt


# linear plot

x = range(5)
y = range(0, 25, 5)

plt.title('Linear plot')
plt.plot(x, y)
plt.xlabel('x - axle')
plt.ylabel('y - axle')
plt.show()

plt.plot(x, y, color='green', marker='o', markersize=10)
plt.title('linear plot beautiful')
plt.show()
