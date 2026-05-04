from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = "sales_management.db"

# ===== Helper: DB connection =====
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # return dict-like rows
    return conn

# ===== GET ALL PRODUCTS =====
@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return jsonify([dict(p) for p in products])

# ===== ADD PRODUCT =====
@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "qty" not in data:
        return jsonify({"error": "Invalid data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, qty) VALUES (?, ?)",
        (data["name"], int(data["qty"]))
    )
    conn.commit()
    conn.close()
    return get_products(), 201

# ===== UPDATE PRODUCT =====
@app.route("/api/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    if not data or "name" not in data or "qty" not in data:
        return jsonify({"error": "Invalid data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE products SET name=?, qty=? WHERE id=?",
        (data["name"], int(data["qty"]), id)
    )
    conn.commit()
    conn.close()
    return get_products()

# ===== DELETE PRODUCT =====
@app.route("/api/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return get_products()

if __name__ == "__main__":
    app.run(debug=True, port=5001)