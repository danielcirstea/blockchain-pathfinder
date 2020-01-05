from matplotlib import pyplot as plt

plt.plot([100, 1000, 2500, 5000, 7500, 10000], [0.0076, 0.46, 2.70, 10.4, 113, 408], label='A1, p=2, q=10, t=1')
# plt.plot([100, 1000, 2500, 5000, 7500, 10000], [0.0022, 0.11, 0.69, 2.68, 16.9, 61.6], label='A2, p=2, q=10, t=1')
plt.plot([100, 1000, 2500, 5000, 7500, 10000], [0.0004, 0.122, 0.593, 2.3, 19.6, 67], label='A1, p=2, q=10, t=1')
# plt.plot([100, 1000, 2500, 5000, 7500, 10000], [0.0001, 0.041, 0.221, 0.818, 3.75, 12.7], label='A2, p=2, q=10, t=1')
plt.xlabel('Number of edges')
plt.ylabel('Time in seconds')
plt.legend()
plt.show()

# 400 initially
