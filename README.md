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

🧩 Technical Challenges

Database Path Errors

Initially trying to access a database file with an incorrect or relative path (../db/store.db) could lead to sqlite3.OperationalError.

Missing Directories (e.g., output/)

Attempting to save charts before ensuring the output directory exists caused FileNotFoundError.

Module Import Errors

Missing libraries like pandas or matplotlib can halt execution until dependencies are installed.

Wrong SQLite3 Installation Assumption

Trying to pip install sqlite3 (which is built-in with Python) resulted in an error and confusion.

Chart Not Updating or Displaying

Forgetting to use plt.tight_layout() or not closing the figure before saving could lead to overlapping chart elements or failed saves.

💻 Environment-Related Challenges

Python Not Recognized

If Python is not added to PATH, commands like python or pip won’t run on terminal.

Different Python Versions

Running into incompatibilities or confusion due to multiple installed versions (e.g., Python 3.13).

Windows-Specific File Handling

Relative paths behave differently on Windows, leading to confusion with '../output' vs 'output'.

🧠 Logical Challenges

Understanding SQL Joins

Combining customer, product, and purchase tables using correct JOIN logic can be tricky.

Datetime Formatting

Extracting the month using strftime('%Y-%m') may be unfamiliar if new to SQL date functions.

Visualization Missteps

Choosing the right type of chart (bar vs. line) or setting axis labels for clarity required thoughtful decisions.

🔄 Debugging Issues

Silent Failures

Some errors (like saving to a non-existent folder) don’t stop the script, making debugging harder.

Database Not Opening

Opening the database before it's populated or without correct permissions results in cryptic SQLite errors.



