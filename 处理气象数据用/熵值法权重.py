import pandas as pd
import numpy as np

def rescale(x, type):
    # 数据归一化函数
    if type == 1:
        return (x - min(x)) / (max(x) - min(x))
    elif type == 2:
        return (max(x) - x) / (max(x) - min(x))

def entropy_weight(X, index):
    # 熵权法计算权重
    pos = np.where(index == 1)[0]
    neg = np.where(index != 1)[0]
    
    # 数据归一化
    X[:, pos] = np.apply_along_axis(rescale, 0, X[:, pos], type=1)
    X[:, neg] = np.apply_along_axis(rescale, 0, X[:, neg], type=2)
    
    # 计算各列权重
    P = X / X.sum(axis=0)
    e = - np.sum(P * np.log(P), axis=0)
    d = 1 - e
    w = d / np.sum(d)
    
    return w

# 读取CSV文件
data = pd.read_csv("your_data.csv")

# 提取指标数据和指示向量
X = data.drop(columns=["index"])  # 假设数据中有一个名为 index 的列表示指示向量
index = data["index"].values

# 计算权重
weights = entropy_weight(X.values, index)

print("各列权重：", weights)