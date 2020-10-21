from app_db import *
import play_scraper
play = Blueprint('play', __name__)
MAX_RESULTS=5
db=mongo.db.play


# ** user and admin both
# Endpoint for search (from db)
@play.route("/<string:q>/", methods=['GET'])
def search(q):
    q=q.replace('+',' ')
    regx = re.compile(q, re.IGNORECASE)
    apps=db.find({"$or":[{"title": regx}, {"developer": regx}, {"id":q}]}).limit(MAX_RESULTS)
    data={}
    # if app already exists, then fetch details from DB
    if apps is not None:
        data=[]
        for app in apps:
            data.append(
                {
                    "id":app["id"],
                    "title":app["title"],
                    "url":app["url"],
                    "developer":app["developer"],
                    "developer_url":app["developer_url"],
                    "icon":app["icon"],
                    "price":app["price"],
                    "developer_email":app['developer_email']
                }
            )
        data=jsonify({"results": data})
    return (data)

# ** user and admin both
# Endpoint for deep search (inserting/updating entries in db)
# Also can be used to insert a single app by app_id
@play.route("/<string:q>", methods=['POST'])
def insert(q):
    q=q.replace(' ','+')
    search=play_scraper.search(q)
    for app in search:
        data={
            "id":app['app_id'],
            "title":str(app['title']),
            "url":"https://play.google.com"+str(app['url']),
            "developer":str(app['developer']),
            "icon":str(app['icon']),
            "price":str(app['price']),
            "developer_url":"https://play.google.com/store/apps/developer?id="+(app['developer'].replace(' ','+')),
            "developer_email":""
        }
        apps=db.find_one({"id":app['app_id']})
        #Saving/Updating the app details to DB
        if apps is None:
            db.insert_one(data)
        else:
            db.update({"id":app['app_id']},{"$set":data})
    q=q.replace(' ','+')
    return redirect(url_for("play.search",q=q))

# ** user and admin both
# Endpoint to refresh/sync for a single app details
@play.route("/sync/<string:id>", methods=['PUT'])
def sync(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        app=play_scraper.details(id)
        data={
            "id":app['app_id'],
            "title":str(app['title']),
            "url":"https://play.google.com"+str(app['url']),
            "developer":str(app['developer']),
            "icon":str(app['icon']),
            "price":str(app['price']),
            "developer_url":"https://play.google.com/store/apps/developer?id="+(app['developer'].replace(' ','+')),
            "developer_email":app['developer_email']
        }
        # Updating the app details to DB
        db.update({"id":id},{"$set":data})
    return jsonify({'result': True})

# ** admin use only
# Endpoint for deleting an app details
@play.route("/<string:id>", methods=['DELETE'])
def delete(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        db.delete_one({"id":id})
    return jsonify({'result': True})

# ** admin use only
# Endpoint for updating an app details
@play.route("/<string:id>", methods=['PUT'])
def update(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        db.update({"id":id},{"$set":request.get_json()})
    return jsonify({'result': True})







