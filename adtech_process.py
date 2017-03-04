from ga_data import process_product_data
from campaign_inventory_updates import aggregate_products_profiles, update_campaign_data
from mysql_connector import PyMYSQLDBConn



__CAMPAIGN = 14


mysql_db_conn = PyMYSQLDBConn()
def get_promoted_products():
	campaign_records = []
	query = "select * from craftsvilla_adsales_campaign where campaign = {0};".format(__CAMPAIGN)
	records = mysql_db_conn.execute_query(query)
	return records

def analytics():
	promoted_products = get_promoted_products()
	product_params={}
	for promoted_product in promoted_products:
		print promoted_product['ProductID']
		product_params['product_id']=promoted_product['ProductID']
		product_params['start_date']=promoted_product['StartDate'].strftime('%Y-%m-%d')
		product_params['end_date']=promoted_product['EndDate'].strftime('%Y-%m-%d')
		product_params['campaign_id']=promoted_product['Campaign']
		process_product_data(product_params)
		aggregate_products_profiles(product_params)
		print "processed analytics for {0}".format(promoted_product['ProductID'])

def init_campaign(campaign=__CAMPAIGN):
	update_campaign_data(campaign)

# analytics()
init_campaign()