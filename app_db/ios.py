from app_db import *
from flask.views import MethodView
ios = Blueprint('ios', __name__)
MAX_RESULTS=5
db=mongo.db.ios

# ** user and admin both
# Endpoint for search (from db)
@ios.route("/<string:q>/", methods=['GET'])
def search(q):
    q=q.replace('+',' ')
    regx = re.compile(q, re.IGNORECASE)
    apps=db.find({"$or":[{"title": regx}, {"publisher": regx}, {"id":q}]}).limit(MAX_RESULTS)
    data={}
    # if app already exists, then fetch details from DB
    if apps is not None:
        data=[]
        for app in apps:
            data.append(
                {
                "id":app["id"],
                "title":app["title"],
                "appURL":app["appURL"],
                "publisher":app["publisher"],
                "publisherURL":app["publisherURL"],
                "icon":app["icon"],
                "price":app["price"],
                "devices":app["devices"],
                }
            )
        data=jsonify({"results": data})
    return (data)

# ** user and admin both
# Endpoint for deep search (inserting/updating entries in db)
# Also can be used to insert a single app by app_id
@ios.route("/<string:q>", methods=['POST'])
def insert(q):
    q=q.replace(' ','+')
    with urllib.request.urlopen('https://itunes.apple.com/search?term='+q+'&entity=iPadSoftware,software&limit=30') as url:
        search = json.loads(url.read().decode())
        search = search['results'] # returns list
    for app in search:
        t_appid=str(app['trackId'])
        # apps=db.find_one({"id":t_appid})
        # if apps is None:

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
        # end of checking devices 
        data={
            "id":t_appid,
            "title":str(app['trackName']),
            "appURL":str(app['trackViewUrl']),
            "publisher":str(app['artistName']),
            "publisherURL":str(app['artistViewUrl']),
            "icon":str(app['artworkUrl512'].replace('512x512','200x200')),
            "price":app.get('formattedPrice',''),
            "devices":str(device),
        }
        apps=db.find_one({"id":t_appid})
        #Saving/Updating the app details to DB
        if apps is None:
            db.insert_one(data)
        else:
            db.update({"id":t_appid},{"$set":data})
    q=q.replace(' ','+')
    return redirect(url_for("ios.search",q=q))

# ** user and admin both
# Endpoint to refresh/sync for a single app details
@ios.route("/sync/<string:id>", methods=['PUT'])
def sync(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        with urllib.request.urlopen('https://itunes.apple.com/search?term='+id+'&entity=iPadSoftware,software&limit=30') as url:
            search = json.loads(url.read().decode())
            search = search['results'] # returns list
        for app in search:
            t_appid=str(app['trackId'])
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
            # end of checking devices 
            data={
                "id":t_appid,
                "title":str(app['trackName']),
                "appURL":str(app['trackViewUrl']),
                "publisher":str(app['artistName']),
                "publisherURL":str(app['artistViewUrl']),
                "icon":str(app['artworkUrl512'].replace('512x512','200x200')),
                "price":app.get('formattedPrice',''),
                "devices":str(device),
            }
            # Updating the app details to DB
            db.update({"id":id},{"$set":data})
    return redirect(url_for("ios.search",q=id))

# ** admin use only
# Endpoint for deleting an app details
@ios.route("/<string:id>", methods=['DELETE'])
def delete(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        db.delete_one({"id":id})
    return jsonify({'result': True})

# ** admin use only
# Endpoint for updating an app details
@ios.route("/<string:id>", methods=['PUT'])
def update(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        db.update({"id":id},{"$set":request.get_json()})
    return jsonify({'result': True})

