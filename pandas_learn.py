# coding=utf-8
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt

catering_sale = 'catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
data=pd.DataFrame(data)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure()
p=data.boxplot()
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
y.sort()

plt.show()