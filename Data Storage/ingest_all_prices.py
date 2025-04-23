import os
import csv
import mysql.connector

def main():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="stockdb"
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_schema = 'stockdb'
          AND table_name   = 'stock_prices'
          AND column_name  = 'adj_close'
    """)
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            ALTER TABLE stock_prices
            ADD COLUMN adj_close DECIMAL(12,4) NULL
              AFTER `close`;
        """)
        conn.commit()
        print("Added column adj_close")

    insert_sql = """
        INSERT INTO stock_prices
          (ticker, date, open, high, low, close, adj_close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    folder = r"C:\Users\USER\Downloads\stock-tweet-and-price\stockprice"
    for fname in os.listdir(folder):
        if not fname.lower().endswith(".csv"):
            continue

        ticker = os.path.splitext(fname)[0]
        path   = os.path.join(folder, fname)
        batch  = []

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                batch.append((
                    ticker,
                    row["Date"],
                    row["Open"],
                    row["High"],
                    row["Low"],
                    row["Close"],
                    row.get("Adj Close") or None,
                    row["Volume"]
                ))

        if batch:
            cursor.executemany(insert_sql, batch)
            conn.commit()
            print(f"{len(batch):4d} rows → {ticker}")

    cursor.close()
    conn.close()
    print("Completed!")

if __name__ == "__main__":
    main()
