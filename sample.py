# app.py

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from database import db_connection
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app,resources={r"/api/*": {"origins": "http://localhost:5173"}})

class Product(Resource):
    def get(self, id=None):
        # dictionary digunakan agar saat pengambilan data dapat berdasarkan field nya, bukan index dari row nya
        cursor = db_connection.cursor(dictionary=True)
        if id:
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            product = cursor.fetchone()
            if product:
                return jsonify(product)
            return {'message': 'Product not found'}, 404
        else:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return jsonify(products)

    def post(self):
        data = request.get_json()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)",
                       (data['name'], data['price']))
        db_connection.commit()
        return {'message': 'Product created'}, 201

    def put(self, id):
        data = request.get_json()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE products SET name=%s, price=%s WHERE id=%s",
                       (data['name'], data['price'], id))
        db_connection.commit()
        return {'message': 'Product updated'}, 200

    def delete(self, id):
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        db_connection.commit()
        return {'message': 'Product deleted'}, 200

api.add_resource(Product, '/api/products', '/api/products/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
