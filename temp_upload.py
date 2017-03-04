from search_analytics import process_changed_inventory
from mysql_connector import PyMYSQLDBConn

conn = PyMYSQLDBConn()

query = "select productid from cv_search_analytics where date>date(current_date-2);";
data = conn.execute_query(query)
products = [field['productid'] for field in data]
process_changed_inventory(products)