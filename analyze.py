import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Connect to database
conn = sqlite3.connect(os.path.join("db", "store.db"))

# === Ensure output directory exists ===
output_dir = os.path.join("output")
os.makedirs(output_dir, exist_ok=True)

# === Top 5 Customers by Spending ===
query1 = """
SELECT c.name, SUM(p.price * pu.quantity) AS total_spent
FROM purchases pu
JOIN customers c ON pu.customer_id = c.id
JOIN products p ON pu.product_id = p.id
GROUP BY c.id
ORDER BY total_spent DESC
LIMIT 5
"""
df1 = pd.read_sql(query1, conn)
plt.figure()
plt.bar(df1['name'], df1['total_spent'], color='skyblue')
plt.title("Top 5 Customers by Spending")
plt.ylabel("Total Spent ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_customers.png"))
print("✅ Chart saved: top_customers.png")

# === Monthly Revenue Trend ===
query2 = """
SELECT strftime('%Y-%m', purchase_date) AS month, 
       SUM(p.price * pu.quantity) AS revenue
FROM purchases pu
JOIN products p ON pu.product_id = p.id
GROUP BY month
ORDER BY month
"""
df2 = pd.read_sql(query2, conn)
plt.figure()
plt.plot(df2['month'], df2['revenue'], marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "monthly_revenue.png"))
print("✅ Chart saved: monthly_revenue.png")

conn.close()
