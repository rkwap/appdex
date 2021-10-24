from app_db import *
import app_db.application as application
from bs4 import BeautifulSoup
uwp = Blueprint('uwp', __name__)
db = mongo.db.uwp

def search_ids(q):
	# Limited to only 8 ids
	q = q.replace(' ','+')
	res = requests.get('https://www.microsoft.com/services/api/v3/suggest?market=en-us&clientId=7F27B536-CF6B-4C65-8638-A0F8CBDFCA65&sources=DCatAll-Products&filter=ExcludeDCatProducts:DCatDevices-Products,DCatSoftware-Products,DCatBundles-Products&counts=10&query='+q).json()
	data = [app['Metas'][0]['Value'] for app in res['ResultSets'][0]['Suggests']]
	return data

def search_ids_slow(q):
	q = q.replace(' ','+')
	apps_res = requests.get('https://www.microsoft.com/en-us/search/shop/apps?q=' + q)
	games_res = requests.get('https://www.microsoft.com/en-us/search/shop/games?q=' + q)
	soup = BeautifulSoup(games_res.content + apps_res.content, 'html.parser')
	res = soup.findAll('div', {'class': 'm-channel-placement-item'})[:25]
	data = [x.find('a').attrs['href'].split('/')[-1] for x in res]
	return data

# ** user and admin both
# Endpoint for deep search (inserting/updating entries in db)
# Also can be used to insert a single app by app_id
@uwp.route("/<string:q>", methods=['POST'])
def insert(q):
	ids = ','.join(search_ids(q))
	print("###########", ids)
	res = requests.post('https://storeedgefd.dsx.mp.microsoft.com/v8.0/sdk/products?market=US&locale=en-us&deviceFamily=Windows.Desktop', data={'productIds': ids}).json()['Products']

	for x in res:
		source = x['LocalizedProperties'][0]
		if x.get('DisplaySkuAvailabilities') is not None and x['DisplaySkuAvailabilities'][0].get('Availabilities') is not None and x['DisplaySkuAvailabilities'][0]['Availabilities'][0].get('OrderManagementData') is not None:
			price = x['DisplaySkuAvailabilities'][0]['Availabilities'][0]['OrderManagementData']['Price']['ListPrice']
			data = {
				'id': x['ProductId'], 
				'title': source['ProductTitle'],
				'icon': 'https:' + source['Images'][0]['Uri'],
				'developer': source['PublisherName'],
				'price': price, 
				'url': 'https://www.microsoft.com/en-us/p/' + re.sub(r'[\W_]+', '-', source['ProductTitle'].lower()) + '/' + x['ProductId'],
				'developer_url': source.get('PublisherWebsiteUri'),
				'developer_email': None,
				'created_at': str(datetime.now()),
				'updated_at': str(datetime.now())
			}
			if db.find_one({"id": x['ProductId']}) is not None: data.pop('created_at')
			db.update({"id": x['ProductId']}, {"$set": data}, upsert=True)
	return redirect(url_for("uwp.search", q=q))

# ** user and admin both
# Endpoint for search (from db)
@uwp.route("/search", methods=['GET'])
def search():
	return application.search(db)

@uwp.route("/find_by_id", methods=['GET'])
def find_by_ids():
	ids = request.args.getlist('ids')
	return application.find_by_ids(ids, db)

# ** admin use only
# Endpoint for deleting an app details
@uwp.route("/<string:id>", methods=['DELETE'])
def delete(id):
	return application.delete(id, db)

# ** admin use only
# Endpoint for updating an app details
@uwp.route("/<string:id>", methods=['PUT'])
def update(id):
	return application.update(id, db)
