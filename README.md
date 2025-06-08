📊 Customer Purchase Analytics

This project analyzes customer purchase data from an SQLite database and generates visual insights such as top spenders and monthly revenue trends using Python.

🧠 Features
Connects to a local SQLite database (store.db)

Calculates total spending by each customer

Identifies top 5 customers by expenditure

Analyzes revenue trends over time (by month)

Saves two charts as .png images:

top_customers.png

monthly_revenue.png

📁 Project Structure

Customer_Purchase_Analytics/

├── db/

│   └── store.db                  # SQLite database

├── scripts/

│   └── analyze.py                # Analysis script

├── output/                       # Folder for charts (auto-created)

│   └── top_customers.png         # Chart 1

│   └── monthly_revenue.png       # Chart 2

💻 Requirements

Python 3.7+

Required packages:

pip install pandas matplotlib

🚀 How to Run

Open terminal and navigate to project directory:

cd Customer_Purchase_Analytics

Run the analysis script:

python scripts/analyze.py

Output:

Charts will be saved to the output/ folder.

✅ Chart saved: top_customers.png

✅ Chart saved: monthly_revenue.png

🐛 Troubleshooting 

Missing database: Ensure db/store.db exists.

Missing output/ folder: The script creates it automatically.

No chart shown: Check if the script ran successfully and no exceptions occurred.

Module not found: Install required libraries with pip.

📈 Sample Output (Charts)

Top 5 Customers by Spending

Monthly Revenue Trend

(You can open the .png files in any image viewer.)

