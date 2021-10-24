from app_db import *
import app_db.application as application
import play_scraper
play = Blueprint('play', __name__)
db = mongo.db.play


# ** user and admin both
# Endpoint for deep search (inserting/updating entries in db)
# Also can be used to insert/update a single app by id
@play.route("/<string:q>", methods=['POST'])
def insert(q):
	q = q.replace(' ', '+')
	search = play_scraper.search(q)
	for app in search:
		data = {
			'id': app['app_id'],
			'title': str(app['title']),
			'icon': str(app['icon']),
			'developer': str(app['developer']),
			'price': str(app['price']),
			'url': 'https://play.google.com'+str(app['url']),
			'developer_url': 'https://play.google.com/store/apps/developer?id='+(app['developer'].replace(' ', '+')),
			'developer_email': None,
			'created_at': str(datetime.now()),
			'updated_at': str(datetime.now())
		}
		if db.find_one({"id": app['app_id']}) is not None: data.pop('created_at')
		db.update({"id": app['app_id']}, {"$set": data}, upsert=True)
	q = q.replace(' ', '+')
	return redirect(url_for("play.search", q=q))


# ** user and admin both
# Endpoint for search (from db)
@play.route("/search", methods=['GET'])
def search():
	return application.search(db)

@play.route("/find_by_id", methods=['GET'])
def find_by_ids():
	ids = request.args.getlist('ids')
	return application.find_by_ids(ids, db)

# ** admin use only
# Endpoint for deleting an app details
@play.route("/<string:id>", methods=['DELETE'])
def delete(id):
	return application.delete(id, db)


# ** admin use only
# Endpoint for updating an app details
@play.route("/<string:id>", methods=['PUT'])
def update(id):
	return application.update(id, db)
