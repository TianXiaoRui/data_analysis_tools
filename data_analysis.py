#数据可视化小工具
import matplotlib.pyplot as plt

filename = '/home/tr/Documents/ScaleFactor.txt'
X, Y = [], []
with open(filename, 'r') as f:  # 1
    lines = f.readlines()  # 2
    for line in lines:  # 3
        value = [float(s) for s in line.split()]  # 4
        X.append(value)  # 5
for i in range(0,len(X)):
    Y.append(i)

print(X)
print(Y)

plt.plot(Y, X)
plt.show()