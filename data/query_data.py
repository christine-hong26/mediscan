import sqlite3

def get_drug_info(drug_name):
    conn = sqlite3.connect('drugs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Drugs WHERE name = ?", (drug_name,))
    drug_info = cursor.fetchone()

    conn.close()
    return drug_info

