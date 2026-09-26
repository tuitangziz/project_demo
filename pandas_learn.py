#import pandas as pd


"""data = {
    "name": ["Tom", "Jack", "Alice"],
    "score": [90, 60, 95],
    "age": [20, 21, 19]
}

df = pd.DataFrame(data)"""

"""print(df)
print(type(df))
print(df.shape)
print(df["name"])
print(df["score"])
print(type(df[["name"]]))
print(type(df["name"]))
print(df["name"])
print(df[["name"]])"""
"""print(type(df["name"]))
print(df[["name", "score"]])
df[df["score"]>=80]#默认会直接输出name是不是因为name是第一个标签
df[(df["score"]>=80)&(df["age"] < 21)]"""
#DataFrame
"""print(df.iloc[2,])
print(df.iloc[1,2])
print(df.loc[1,"score"])
print(df.loc[df["score"]>=80,["name","score"]])"""
#因为df.iloc[1, 2]中的2，就是第三列，正好就是age
"""df = pd.DataFrame({
    "name": ["Tom", "Jack", "Alice", "Bob"],
    "score": [90, 55, 95, 70],
    "age": [20, 21, 19, 22]
})
df["bonus_score"]=df["score"]+5
df["passed"]=df["score"]>=60
df.loc[1,"score"]=65
df.loc[df["age"]>20,"age"]=100#用loc，第一个参数一定是要加df前缀表示对行的限制或者理解为从列的某个标签找一行，而第二个参数一定是“”这样的，里面必须是列的标签一个或多个都行
sorted_df=df.sort_values("score", ascending=False)"""

"""df = pd.read_csv("students.csv")
print(df.head(3))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df[df["score"]>=80])
print(df.sort_values("score", ascending=False))
df["passed"]=df["score"]>=60"""
"""df=pd.read_csv("students.csv")
print(df)
print(df.isna().sum())
df_scoreless=df["score"].isna()
print(df[df_scoreless])
clean_df=df.dropna()
fill_df=df.copy()
fill_df["score"]=df["score"].fillna(df["score"].mean())
fill_df["age"]=df["age"].fillna(0)
print(fill_df)
print(clean_df)"""
"""df = pd.DataFrame({
    "id": [1, 2, 3, 1, 4],
    "name": [" Tom ", "JACK", "alice", " Tom ", "Bob"],
    "score": [90, 60, 95, 90, 70]
})"""
"""print(df.duplicated())
clean_df=df.drop_duplicates(subset=["id"])
clean_df["name"]=clean_df["name"].str.strip()
clean_df["name"]=clean_df["name"].str.lower()
clean_df=clean_df.sort_values("score", ascending=False)
print(clean_df)"""

"""df = pd.DataFrame({
    "name": ["Tom", "Jack", "Alice", "Bob", "David", "Lucy"],
    "class": ["A", "A", "B", "B", "A", "B"],
    "gender": ["M", "M", "F", "M", "F", "F"],
    "score": [90, 60, 95, 70, 80, 85]
})
df.groupby("class")["score"].mean()
df.groupby("class")["score"].max()
df.groupby("class")["score"].min()
df.groupby("class")["score"].count()
#df_better80=df[df["score"]>=80].copy()
#print(df_better80.groupby("class")["score"].count())
#懒得测试了应该没问题
df.groupby("class")["score"].agg(["mean", "max","min","count"])#你没说用score我默认了
print(df.groupby("class").value_counts())#理论上应该是以class作为区分，剩下的区分并计数，这一部分规则还有点模糊，难道是除了class的数据必须保留？我猜
#下面的这个应该是答案。上面的和下下面的是我有点晕再理清思路
print(df["class"].value_counts())#只关注class这个标签下的数据，然后对class标签下的数据区分并计数
print(df.groupby("class").count())#以class作为区分，剩下的再各自计数，除了class的数据都保留了
print(df.groupby("class"))#只是映射
print(df["gender"].value_counts())#第三题
print(df.groupby(["gender","class"])["score"].mean())#4
df_better80=df[df["score"]>=80].copy()
df_better80["gender"].value_counts()"""
"""students = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Tom", "Jack", "Alice", "Bob"]
})

scores = pd.DataFrame({
    "id": [3, 1, 2, 5],
    "score": [95, 90, 60, 100]
})
1,2,3
1,2,3,4
pd.merge(students,scores,on="id")
pd.merge(students,scores,on="id",how="left")"""
#Bob
#不会，因为左边没有id=5的人
"""df = pd.DataFrame({
    "name": ["Tom", "Jack", "Alice", "Bob"],
    "age": [20, 21, 19, 22],
    "score": [90, 60, 95, 70]
})
df.info()
print(df.describe())
df["passed"]=df["score"]>=60
df=df[df["score"]>=70]
df=df.sort_values("score", ascending=False)
df.to_csv("students.csv",index=False)"""
"""import pandas as pd
df=pd.read_csv("students.csv")
cl=pd.read_csv("class.csv")
print(df.shape)
print(df.info())
df.isna().sum()#这个我忘了找你提示
df_drop=df.drop_duplicates(subset="id").copy()
df_drop["name"]=df_drop["name"].str.strip()
df_drop["name"]=df_drop["name"].str.lower()
df_drop["score"]=df_drop["score"].fillna(df_drop["score"].mean())
df_drop["age"]=df_drop["age"].fillna(0)
df_drop["passed"]=df_drop["score"]>=60
clean_student_class=pd.merge(df_drop,cl,on="class_id",how="left")
good_students=clean_student_class[clean_student_class["score"]>=70]
good_students=good_students.sort_values("score", ascending=False)
df_mean=good_students.groupby("class_name")["score"].mean()
df_min=good_students.groupby("class_name")["score"].min()
df_max=good_students.groupby("class_name")["score"].max()
df_count=good_students.groupby("class_name")["score"].count()
good_students.to_csv("clean_students.csv",index=False)#很多看了之前写的代码
pd.concat([df_mean,df_min,df_max,df_count],axis=1).to_csv("class_summary.csv")#网上查的，我看了结果发现我的name没，不懂
"""
import pandas as pd

# 1. 读取
df = pd.read_csv("students.csv")
cl = pd.read_csv("class.csv")

# 2. 检查
print(df.shape)
df.info()
print(df.isna().sum())

# 3. 去重
df_drop = df.drop_duplicates(subset=["id"]).copy()

# 4. 字符串清洗
df_drop["name"] = df_drop["name"].str.strip()
df_drop["name"] = df_drop["name"].str.lower()

# 5. 填补缺失值
df_drop["score"] = df_drop["score"].fillna(
    df_drop["score"].mean()
)

df_drop["age"] = df_drop["age"].fillna(0)

# 6. 新字段
df_drop["passed"] = df_drop["score"] >= 60

# 7. 合并班级表
clean_student_class = pd.merge(
    df_drop,
    cl,
    on="class_id",
    how="left"
)

# 8. 筛选 >= 70
good_students = clean_student_class[
    clean_student_class["score"] >= 70
].copy()

# 9. 排序
good_students = good_students.sort_values(
    "score",
    ascending=False
)

# 10. 班级统计
class_summary = (clean_student_class.groupby("class_name")["score"].agg(["mean", "max", "min", "count"]) .reset_index())
#或者
class_summary = clean_student_class.groupby("class_name")["score"].agg(["mean","max","min","count"])
# 11. 保存清洗后的完整数据
clean_student_class.to_csv(
    "clean_students.csv",
    index=False
)

# 12. 保存班级统计
class_summary.to_csv(
    "class_summary.csv",
    index=False
)