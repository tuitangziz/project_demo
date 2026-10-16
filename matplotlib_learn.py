import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([12, 13, 24, 35])

line_styles = dict(marker=".",
                   markersize=30,
                   markerfacecolor="red",
                   markeredgecolor="blue",
                   linestyle="solid",
                   linewidth=2,)
                  # color="black")

plt.title("Class size", fontsize=20,
                              family="Arial",
                              fontweight="bold",
                              color="blue",)

plt.xlabel("Year", fontsize=20,
                          family="Arial",
                          fontweight="bold",
                          color="#a742f5")

plt.ylabel("Students", fontsize=20,
                              family="Arial",
                              fontweight="bold",
                              color="#a742f5")

plt.tick_params(axis="both",
                colors="#85d424",)

plt.plot(x, y1, color="#6ff707", **line_styles)
plt.plot(x, y2, color="#25b3a4", **line_styles)
plt.plot(x, y3, color="#de59af", **line_styles)

plt.xticks(x)

plt.show()"""

"""x = [1,2,3,4,5]
y = [5,10,15,20,25]

plt.grid(axis="x",
         linewidth=2,
         color="lightgray",
         linestyle="dashed",)

plt.plot(x,y)
plt.show()"""



"""categories = ["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"]
values = [4, 3, 2, 5, 3, 1]

# plt.bar(categories, values,color="skyblue")
plt.barh(categories, values,color="skyblue")#但是改成水平条形图之后标签没说咋改

plt.title("Daily Consumption")
plt.ylabel("Food")
plt.xlabel("Quantity")

plt.tight_layout()
plt.show()"""



"""categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = [300, 250, 275, 225]
colors = ["red", "green", "blue", "yellow"]

plt.pie(values,labels=categories,
               autopct="%1.1f%%",
               colors=colors,
               explode=[0,0,0,0.04],
               shadow=True,
               startangle=90)

plt.title("Bro Code Colledge")

plt.show()"""



"""x1 = [0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]
y1 = [55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]

x2 = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]
y2 = [50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97]

plt.scatter(x1, y1, color="skyblue",
                  alpha=0.5,
                  s = 10,
                  label="Class A",)

plt.scatter(x2, y2, color="red",
                  alpha=0.5,
                  s = 10,
                  label="Class B")

plt.title("Test Scores")
plt.xlabel("Hour Study")
plt.ylabel("Grade")

# plt.tight_layout()
plt.legend()
plt.show()"""


# np.random.seed(10)
"""scores = np.random.normal(loc=80, scale=10, size=100)#你只教我了random.rand这个我大概理解但是没系统性学习
scores = np.clip(scores, 0, 100)
plt.hist(scores, bins=20,
                 color="lightgreen",
                 edgecolor="black")

plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("# of Students")

plt.show()"""



"""x = np.array([1, 2, 3, 4, 5])

figure,axes = plt.subplots(2,2)

axes[0,0].plot(x,x*2,color="red")
axes[0,0].set_title("x*2")

axes[0,1].plot(x,x**2,color="blue")
axes[0,1].set_title("x**2")

axes[1,0].bar(x,x**3,color="green")
axes[1,0].set_title("x**3")

axes[1,1].plot(x,x**10,color="purple")
axes[1,1].set_title("x**10")

plt.tight_layout()
plt.show()"""



"""df = pd.read_csv("data.csv")
type_count = df["Type1"].value_counts(ascending=True)#value_counts学过吗，有点忘了

plt.barh(type_count.index, type_count.values,color="blue",
                                             edgecolor="black",)

plt.title("# of Pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()"""



months = np.array([1, 2, 3, 4, 5, 6])
sales = np.array([20, 24, 23, 30, 35, 40])
ad_cost = np.array([2, 3, 2.5, 4, 5, 6])

ages = np.array([
    18, 20, 21, 22, 22, 23, 24, 24, 25, 26,
    27, 28, 28, 29, 30, 31, 32, 33, 35, 40
])

df = pd.DataFrame({
    "type": [
        "A", "B", "A", "C", "A",
        "B", "B", "C", "A", "B"
    ]
})

figure,axes = plt.subplots(2,2)

axes[0,0].plot(months, sales, color="blue")
axes[0,0].set_title("Sales for month")
axes[0,0].set_xlabel("Month")

axes[0,1].bar(df["type"].value_counts().index,df["type"].value_counts().values,color="blue")
axes[0,1].set_title("Type for times")
axes[0,1].set_xlabel("Type")

axes[1,0].scatter(ad_cost,sales , color="red")
axes[1,0].set_title("Ad cost fot Sales")
axes[1,0].set_xlabel("Ad cost")

axes[1,1].hist(ages, color="purple")
axes[1,1].set_title("Ages")

plt.tight_layout()
plt.show()