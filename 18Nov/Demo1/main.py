import cx_Oracle

##Fetching DB details
db_detail_list = []
db_detail_dict = {}
with open('connect.config') as config_file:
	db_detail_list = config_file.readlines()
for db_detail in db_detail_list:
	db_detail_dict[db_detail.split(':')[0]]=db_detail.strip().split(':')[1]
##Fetching Validation Queries
sql_list = []
with open('validation_queries.sql') as content:
	sql_list = [i.strip() for i in content.readlines()]

##Initiating connection
conn = f"{db_detail_dict['user/pass']}@(description=(address=(protocol=tcp)\
(host={db_detail_dict['host']})(port={db_detail_dict['default_port']}))\
(connect_data=(sid={db_detail_dict['custDB']})))"

connection = cx_Oracle.connect(conn)
rows = []
results = []
with connection as db:
	cursor = db.cursor()
	cursor.execute(sql_list[0])
	rows = [i[0] for i in cursor.description]
	results = cursor.fetchall()
print(rows, results)
if results[0][0] == 5:
	print('validation successful')
