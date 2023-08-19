import matplotlib.pyplot as plt


vals = [24, 17, 53, 21, 35]
labels = ['Ford', 'Audi', 'Toyota', 'BMW', 'Mercedes']

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title('Cars pie')
plt.show()
