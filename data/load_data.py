import sqlite3
import csv

def load_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('drugs.db')
    cursor = conn.cursor()

    # Load the CSV file into the database
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
    load_data()
