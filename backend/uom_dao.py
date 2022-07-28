from database import get_sql_connection
def get_uoms(connection):
    cur = connection.cursor()
    query = "SELECT * FROM uom"
    cur.execute(query)
    connection.commit()
    response = []
    for (uom_id, uom_name) in cur:
        response.append({
            'unit_id': uom_id,
            'unit_name': uom_name
        })
    cur.close()
    return response

