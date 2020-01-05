import matplotlib.pyplot as plt
import statistics

# objects = ('42 (1)', '127 (2)', '10645 (3)', '126666 (4)')
# performance = [0, 7, 10, 1669]

# ('a67f (79600)', '0361 (19981)', 'a359 (29875)', '8549 (10000)', 'c81b (28524)',
# 'ee1a (14236)', '1e32 (59806)', '4a5d (9999)', 'e21e (19966)', 'c6e7 (9999)')

objects = ('a67f', '0361', 'a359', '8549', 'c81b',
           'ee1a', '1e32', '4a5d', 'e21e', 'c6e7')
performance = [50.95, 12.80, 19.13, 6.40, 18.28, 9.1, 38.31, 6.40, 12.79, 6.40]

# y_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# plt.bar(y_pos, performance)
# plt.xticks(y_pos, objects)
# plt.ylabel('Memory occupied (MB)')
# plt.xlabel('Transaction data represented by root nodes')
# plt.show()

print(statistics.mean(performance))
