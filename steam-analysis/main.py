import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
df = pd.read_csv("steam.csv")

print("==== データ確認 ====")
print(df.head())

# プレイヤー数ランキング
ranking = df.sort_values("players", ascending=False)
print("==== プレイヤーランキング ====")
print(ranking.head())

# ジャンル別プレイヤー数
genre_players = df.groupby("genre")["players"].sum()

# グラフ作成
plt.figure(figsize=(10,6))

genre_players.plot(kind="bar")

plt.title("Steam Players by Genre")
plt.xlabel("Genre")
plt.ylabel("Players")
plt.xticks(rotation=45)

plt.tight_layout()

# 画像保存
plt.savefig("genre_players.png")

plt.show()

# ===== 無料ゲーム vs 有料ゲーム =====

free_vs_paid = df.groupby(df["price"] == 0)["players"].mean()

print("==== Free vs Paid Average Players ====")
print(free_vs_paid)

# グラフ作成
free_vs_paid.plot(kind="bar")

plt.title("Free vs Paid Games Average Players")
plt.xlabel("Free Game (True = Free)")
plt.ylabel("Average Players")

plt.tight_layout()

plt.savefig("free_vs_paid.png")

plt.show()

# Free vs Paid Games
free_vs_paid = df.groupby(df["price"] == 0)["players"].mean()

free_vs_paid.plot(kind="bar")

plt.title("Free vs Paid Games Average Players")
plt.xlabel("Free Game")
plt.ylabel("Average Players")

plt.tight_layout()

plt.savefig("free_vs_paid.png")

plt.show()
