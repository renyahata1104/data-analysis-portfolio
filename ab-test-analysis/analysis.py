import pandas as pd
from scipy import stats

df = pd.read_csv("ab_data.csv")

group_A = df[df["group"] == "A"]["converted"]
group_B = df[df["group"] == "B"]["converted"]

t_stat, p_value = stats.ttest_ind(group_A, group_B)

print("A conversion:", group_A.mean())
print("B conversion:", group_B.mean())
print("p-value:", p_value)