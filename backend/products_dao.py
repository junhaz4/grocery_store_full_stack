from database import get_sql_connection

def get_all_products(connections):
    cur = connections.cursor()
    query = "select products.product_id, products.name, products.unit_id, products.price_per_unit, uom.unit_name from products inner join uom on products.unit_id = uom.unit_id;"
    cur.execute(query)
    connections.commit()
    response = []
    for (product_id, name, unit_id, price_per_unit,unit_name) in cur:
        response.append({
            'product_id': product_id,
            'name': name,
            'unit_id': unit_id,
            'price_per_unit': price_per_unit,
            'unit_name': unit_name
        })
    cur.close()
    return response

def delete_product(connection, product_id):
    cur = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cur.execute(query)
    connection.commit()
    cur.close()
    return cur.lastrowid

def insert_new_product(connection, product):
    cur = connection.cursor()
    query = ("INSERT INTO products (name, unit_id, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price_per_unit'])

    cur.execute(query, data)
    connection.commit()
    cur.close()
    return cur.lastrowid

