import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
df = pd.read_csv("customer_orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

snapshot_date = df["order_date"].max() + pd.Timedelta(days=1)

rfm = df.groupby("customer_id").agg({
    "order_date": lambda x: (snapshot_date - x.max()).days,
    "order_id": "count",
    "amount": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print(rfm)

rfm["Monetary"].plot(kind="bar")

plt.title("Customer Monetary Value")
plt.xlabel("Customer")
plt.ylabel("Total Spending")

plt.tight_layout()

plt.savefig("rfm_monetary.png")
