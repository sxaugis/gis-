import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import pandas as pd

def sliding_t_test(data,window_size):
  n = len(data)
  p_values = []
  for i in range(n - window_size + 1):
    group1 = data[i:i + window_size]
    group2 = data[i + window_size:]
    t_stat, p_value = ttest_ind(group1, group2)
    p_values.append(p_value)
  return p_values

data = pd.read_excel('D:\gis\数据\论文\梁\数据\lianxu.xlsx')
data = data.iloc[:,0].values

window_size = 10
p_values = sliding_t_test(data, window_size)

plt.plot(range(window_size, len(data)+1), p_values)
plt.xlabel('Time')
plt.ylabel('P value')
plt.title('Sliding t test')
plt.show()