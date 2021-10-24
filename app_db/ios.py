from app_db import *
import app_db.application as application
ios = Blueprint('ios', __name__)
MAX_RESULTS=5
db = mongo.db.ios

# ** user and admin both
# Endpoint for deep search (inserting/updating entries in db)
# Also can be used to insert a single app by app_id
@ios.route("/<string:q>", methods=['POST'])
def insert(q):
	q = q.replace(' ','+')
	search = requests.get('https://itunes.apple.com/search?term=' + q + '&entity=iPadSoftware,software&limit=30').json()['results']
	for app in search:
		# Checking for devices supported 
		for device in app['supportedDevices']:
			if 'iPhone' in device:
				iPhone = True
				break
			else:
				iPhone = False
		for device in app['supportedDevices']:
			if 'iPad' in device:
				iPad = True
				break
			else:
				iPad = False
		if iPhone is False :
			device = "iPad Only"
		if iPad is False :
			device = "iPhone Only" 
		if iPhone is True and iPad is True :
			device = "Both iPhone and iPad"  
		price=app.get('formattedPrice','')
		if price=="Free":
			price="0"
		# end of checking devices 
		data = {
			"id":str(app['trackId']),
			"title":str(app['trackName']),
			"icon":str(app['artworkUrl512'].replace('512x512','200x200')),
			"developer":str(app['artistName']),
			"price":price,
			"url":str(app['trackViewUrl']),
			"developer_url":str(app['artistViewUrl']),
			'developer_email': None,
			"devices":str(device),
			'created_at': str(datetime.now()),
			'updated_at': str(datetime.now())
		}
		if db.find_one({"id": str(app['trackId'])}) is not None: data.pop('created_at')
		db.update({"id": str(app['trackId'])}, {"$set": data}, upsert=True)
	q = q.replace(' ','+')
	return redirect(url_for("ios.search",q = q))


# ** user and admin both
# Endpoint for search (from db)
@ios.route("/search", methods=['GET'])
def search():
	return application.search(db)

@ios.route("/find_by_id", methods=['GET'])
def find_by_ids():
	ids = request.args.getlist('ids')
	return application.find_by_ids(ids, db)

# ** admin use only
# Endpoint for deleting an app details
@ios.route("/<string:id>", methods=['DELETE'])
def delete(id):
	return application.delete(id, db)


# ** admin use only
# Endpoint for updating an app details
@ios.route("/<string:id>", methods=['PUT'])
def update(id):
	return application.update(id, db)
