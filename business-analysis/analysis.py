import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# カテゴリ別売上
category_sales = df.groupby("category")["amount"].sum()

print(category_sales)

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.savefig("sales_trend.png")
plt.show()