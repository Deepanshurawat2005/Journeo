import os
import mysql.connector
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

url = os.getenv("DATABASE_URL")

parsed = urlparse(url)

connection = mysql.connector.connect(
    host=parsed.hostname,
    port=parsed.port,
    user=parsed.username,
    password=parsed.password,
    database=parsed.path.lstrip("/")
)

if connection.is_connected():
    print("✅ MySQL connection successful!")

cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")

database = cursor.fetchone()[0]
print(f"✅ Connected database: {database}")

cursor.close()
connection.close()