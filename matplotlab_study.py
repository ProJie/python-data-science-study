# coding=utf-8
import matplotlib.pyplot as plt
import sys

import numpy

reload(sys)
sys.setdefaultencoding('utf-8')

year = [1900, 1930, 1960, 1990]

pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.fill_between(year, pop, 0, color='green')
plt.xlabel('Year')
plt.ylabel('POP')
plt.title('Lines')
plt.show()
