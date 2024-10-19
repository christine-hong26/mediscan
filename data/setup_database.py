import csv
import sqlite3

def setup_database():
    # Connect to the SQLite database (or create it)
    conn = sqlite3.connect('drugs.db')
    cursor = conn.cursor()

    # Create the table based on your schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Drugs (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            substitute1 TEXT,
            substitute2 TEXT,
            substitute3 TEXT,
            substitute4 TEXT,
            side_effect1 TEXT,
            side_effect2 TEXT,
            side_effect3 TEXT,
            treatment TEXT,
            status TEXT,
            class TEXT,
            notes TEXT
        )
    ''')

    with open('medicine_dataset.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row if there's one
        for row in reader:
            cursor.execute('''
                INSERT OR REPLACE INTO Drugs (id, name, substitute1, substitute2, substitute3, substitute4, 
                                  side_effect1, side_effect2, side_effect3, treatment, status, class, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4], row[5], 
                row[6], row[7], row[8], row[9], row[10], row[11], row[12]))


    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()