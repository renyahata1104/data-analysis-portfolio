-- 総売上
SELECT SUM(amount) AS total_sales
FROM sales;

-- 商品別売上
SELECT product, SUM(amount) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC;

-- カテゴリ別売上
SELECT category, SUM(amount) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- 顧客別売上ランキング
SELECT customer_id, SUM(amount) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC;

-- 月別売上
SELECT 
strftime('%Y-%m', order_date) AS month,
SUM(amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;
