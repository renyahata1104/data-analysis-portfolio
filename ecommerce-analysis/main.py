import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
df = pd.read_csv("sales.csv")

# 売上列作成
df["sales"] = df["price"] * df["quantity"]

print("=== データ確認 ===")
print(df.head())

# 商品別売上
product_sales = df.groupby("product")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("product_sales.png")


# カテゴリ別売上
category_sales = df.groupby("category")["sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("category_sales.png")

# 日付をdatetime型に変換
df["order_date"] = pd.to_datetime(df["order_date"])

# 月列作成
df["month"] = df["order_date"].dt.to_period("M")

# 月別売上
monthly_sales = df.groupby("month")["sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("monthly_sales.png")