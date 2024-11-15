import sqlite3
from webscrape import webscrape 

# Initialize the SQLite database
def initialize_database():
    conn = sqlite3.connect("scraped_data.db")
    cursor = conn.cursor()

    # Create a table to store scraped data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ScrapedData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            element_type TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_scraped_data(url, element_type, content):
    conn = sqlite3.connect("scraped_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ScrapedData (url, element_type, content)
        VALUES (?, ?, ?)
    """, (url, element_type, content))

    conn.commit()
    conn.close()

# Function to fetch all data from the database
def fetch_all_data():
    conn = sqlite3.connect("scraped_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ScrapedData")
    rows = cursor.fetchall()

    conn.close()
    return rows

# Scraping and storing data
def scrape_and_store(url, element_type):
    # Get elements using the webscrape class
    scraped_texts = webscrape.get_elements(url, element_type)

    if scraped_texts:
        for text in scraped_texts:
            insert_scraped_data(url, element_type, text)

def clear_table(table_name):
    try:
        # Connect to the database
        conn = sqlite3.connect("scraped_data.db")
        cursor = conn.cursor()

        # Clear the table
        cursor.execute(f"DELETE FROM {table_name};")

        # Optionally, reset the auto-increment counter (if applicable)
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = '{table_name}';")

        conn.commit()
        print(f"Table '{table_name}' cleared successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        conn.close()

def print_all_tables(database):
    try:
        # Connect to the database
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Query to list all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Print the table names
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        conn.close()


if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # URL and element type to scrape
    test_url = "https://brandeisjudges.com/sports/2023/7/24/gosman-sports-and-convocation-center.aspx"
    element_type = "h3"  # For example, scrape all <h3> tags

    # Scrape and store data
    scrape_and_store(test_url, element_type)

    # Fetch and display all data from the database
    all_data = fetch_all_data()
    for row in all_data:
        print(row)
 

# uncomment below to clear table
# clear_table("ScrapedData") 
