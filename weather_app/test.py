import sqlite3

# Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect('/Users/suneetha.porumamilla/Desktop/weather-dashboard.db')
cursor = conn.cursor()


cursor.execute("SELECT * FROM user_accounts")
results = cursor.fetchall()
for row in results:
    print(row)

# Close connection
conn.close()