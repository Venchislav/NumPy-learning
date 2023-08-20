import matplotlib.pyplot as plt

labels = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']

android = [65, 65.9, 69, 71, 80, 60, 65]
ios = [34.7, 33.1, 30.01, 28.1, 19.05, 32.01, 32.001]

width = 0.35
fig, ax = plt.subplots()

ax.bar(labels, android, width, label='Android', color='green')
ax.bar(labels, ios, width, bottom=android, label='IOS', color='grey')

ax.set_ylabel('Sells')
ax.set_title('Android and IOS sells')
ax.legend(loc='lower left', title='Devices')

plt.show()
