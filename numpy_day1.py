#import numpy as np
"""a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a.mean())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.shape)

print(a)
c=np.ones((1,1))
print(c)
d=np.arange(0,10,1)
print(d)
f=np.random.rand(9, 9)*10
print(f)
print(f.dtype)
a=np.array([10,20,30])
a=a.astype(float)
(2,3)
[[1,4],[2,5],[3,6]]
(3,2)
(3,)
(3,)
(3,1)
(2,2)
[[1 2] [3 4] [5 6] [7 8]]
shape(4,2)
(6,)
(2,3)
scores = np.array([0.1, 0.7, 0.2])
scores.max()
print(f"{scores.max()}是第{scores.argmax()+1}个")
[1 0 2]
a = np.array([20, 55, 80, 40, 95])
print(a[a>=60])
np.where(a >= 60, 1, 0)
np.where(a >= 60, a, 0)
[1 2 100 4 5]
[2 100 4]
[1 2 3 4 5]
[2 100 4]"""
"""import numpy as np

scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [95, 88, 92],
    [50, 65, 55],
    [78, 82, 80]
])
print(scores.mean(axis=1))#这是我试了一次才知道应该=1
print(scores.mean(axis=0))
stdunt_mean=scores.mean(axis=1)
print(stdunt_mean[stdunt_mean>=80])
new_scores=scores.copy()
new_scores[new_scores<60]=0
scores.argmax(axis=1)
print(scores.argmax(axis=1))
scores.max()
print(scores.max(axis=1))"""
#其实有很多我都是看来你的提示的，不过我没有往前翻你发过的，或者看笔记，不会就多试了几次
import numpy as np

data = np.array([
    [170, 60],
    [180, 80],
    [160, 50],
    [190, 90]
], dtype=float)
data_mean=data.mean(axis=0)
data_std=data.std(axis=0)
standardized=(data - data_mean)/data_std
print(standardized)
print(standardized.mean(axis=0))
print(standardized.std(axis=0))