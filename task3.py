import matplotlib.pyplot as plt

ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
frequency = [10, 15, 25, 30, 20, 15, 10, 5, 2, 1]

plt.bar(ages, frequency, color='blue', alpha=0.7)

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')

plt.show()
import matplotlib.pyplot as plt

ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.hist(ages, bins=10, color='green', edgecolor='black', alpha=0.7)

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')

plt.show()