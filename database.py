import sqlite3

with sqlite3.connect("sales_management.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        qty INTEGER NOT NULL
    )
    """)
    
    # Optional: Preload products
    products = [
        "afroComb", "afro-combs", "Bamana-tji-wara", "barefoot-beads",
        "bass-harp", "ceramic-pots", "ceremonial-swords", "face-mask",
        "figi-guide", "gourd-shaker", "grassland-mask", "horn",
        "india-sloan", "leather-apron", "maracas", "maasai-gourd",
        "shekere-coweries", "shell-neckless", "Threaded-coweries",
        "Tkar-horns", "traditional-bowls", "tribal-drums",
        "turkana-apron", "waste", "wooden-mask", "wooden-plate"
    ]
    
    for p in products:
        cursor.execute("INSERT INTO products (name, qty) VALUES (?, ?)", (p, 10))
    
    conn.commit()

print("Database and products ready!")