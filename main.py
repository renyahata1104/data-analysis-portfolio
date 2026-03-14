import pandas as pd
import matplotlib.pyplot as plt

# =========================
# データ読み込み
# =========================
df = pd.read_csv("games.csv")

print("===== データ確認 =====")
print(df)

# =========================
# 人気ゲームランキング
# =========================
print("===== 人気ゲームランキング =====")
ranking = df.sort_values("players", ascending=False)
print(ranking)

# =========================
# ジャンル別プレイヤー数
# =========================
print("===== ジャンル別プレイヤー数 =====")
genre_players = df.groupby("genre")["players"].sum()
print(genre_players)

# =========================
# ジャンル別シェア
# =========================
print("===== ジャンル別シェア (%) =====")
genre_share = genre_players / genre_players.sum() * 100
print(genre_share)

# =========================
# リリース年別プレイヤー数
# =========================
print("===== リリース年別プレイヤー数 =====")
year_players = df.groupby("release_year")["players"].sum()
print(year_players)

# =========================
# リリース年別ゲーム数
# =========================
print("===== リリース年別ゲーム数 =====")
year_count = df.groupby("release_year")["game"].count()
print(year_count)

# =========================
# 上位3ゲームのシェア
# =========================
print("===== 上位3ゲームのシェア (%) =====")
top3_share = ranking.head(3)["players"].sum() / df["players"].sum() * 100
print(top3_share)

# =========================
# グラフ① ジャンル別プレイヤー数
# =========================
genre_players.plot(kind="bar")
plt.title("Players by Genre")
plt.xlabel("Genre")
plt.ylabel("Players")
plt.tight_layout()
plt.savefig("genre_players.png")
plt.close()

# =========================
# グラフ② 人気ゲームランキング
# =========================
ranking.plot(x="game", y="players", kind="bar")
plt.title("Game Popularity Ranking")
plt.xlabel("Game")
plt.ylabel("Players")
plt.tight_layout()
plt.savefig("game_ranking.png")
plt.close()

# =========================
# グラフ③ ジャンル別シェア
# =========================
genre_share.plot(kind="pie", autopct="%1.1f%%")
plt.title("Genre Share")
plt.ylabel("")
plt.tight_layout()
plt.savefig("genre_share.png")
plt.close()

# =========================
# グラフ④ リリース年別プレイヤー数
# =========================
year_players.plot(kind="bar")
plt.title("Players by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Players")
plt.tight_layout()
plt.savefig("year_players.png")
plt.close()

# =========================
# グラフ⑤ リリース年別ゲーム数
# =========================
year_count.plot(kind="bar")
plt.title("Number of Games by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("year_count.png")
plt.close()

print("===== グラフ保存完了 =====")
print("genre_players.png")
print("game_ranking.png")
print("genre_share.png")
print("year_players.png")
print("year_count.png")
