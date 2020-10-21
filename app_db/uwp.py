from app_db import *
import os
from bs4 import BeautifulSoup, SoupStrainer
import http.cookiejar
from multiprocessing import Pool
uwp = Blueprint('uwp', __name__)
MAX_RESULTS=5
db=mongo.db.uwp

all_urls=list()

def search_ids(q):
    q = q.replace(' ','+')
    page = requests.get('https://www.microsoft.com/services/api/v3/suggest?clientId=7F27B536-CF6B-4C65-8638-A0F8CBDFCA65&sources=Iris-Products%2CDCatAll-Products%2CMicrosoft-Terms&query='+q)
    soup = BeautifulSoup(page.text, 'html.parser')
    raw=dict(json.loads(str(soup)))
    raw=raw["ResultSets"][0]["Suggests"]
    data=[]
    for app in raw:
        data.append(app["Metas"][0]["Value"])
    return data


def get_app(id):
    # Scraping the app details
    cookie_file='/tmp/cookies'
    cj=http.cookiejar.LWPCookieJar(cookie_file)
    try:
        cj.load()
    except:
        pass
    s = requests.Session() 
    s.cookies = cj
    url= 'https://www.microsoft.com/en-us/p/app/'+id
    page = s.get(url,cookies=cj).content
    soup = BeautifulSoup(page, 'html.parser')
    data={
        "id": id,
        "title": soup.find('h1', {'id':'DynamicHeading_productTitle'}).text,
        "developer": (str(soup.find('div', {'aria-label':'Published by'}).find('span').text).encode('ascii', 'ignore')).decode("utf-8"),
        "icon": (soup.find('meta', {'property':'og:image'}).attrs['content']),
        "price": soup.find('meta', {'itemprop':'price'}).attrs['content'],
        "url" : url
    }
    cj.save(ignore_discard=True)
    return (data)

# ** user and admin both
# Endpoint for search (from db)
@uwp.route("/<string:q>/", methods=['GET'])
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
                    "icon":app["icon"],
                    "price":app["price"],
                }
            )
        data=jsonify({"results": data})
    return (data)

# ** user and admin both
# Endpoint for deep search (inserting/updating entries in db)
# Also can be used to insert a single app by app_id
@uwp.route("/<string:q>", methods=['POST'])
def insert(q):
    q=q.replace(' ','+')
    search=search_ids(q)

    all_urls=['https://www.microsoft.com/en-us/p/app/'+id for id in search]
    
    for id in search:
        data=get_app(id)
        apps=db.find_one({"id":id})
        #Saving/Updating the app details to DB
        if apps is None:
            db.insert_one(data)
        else:
            db.update({"id":id},{"$set":data})
    q=q.replace(' ','+')
    # return redirect(url_for("uwp.search",q=q))
    return jsonify({'result': True})


# ** user and admin both
# Endpoint to refresh/sync for a single app details
@uwp.route("/sync/<string:id>", methods=['PUT'])
def sync(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        data=get_app(id)
        # Updating the app details to DB
        db.update({"id":id},{"$set":data})
    return jsonify({'result': True})


# ** admin use only
# Endpoint for deleting an app details
@uwp.route("/<string:id>", methods=['DELETE'])
def delete(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        db.delete_one({"id":id})
    return jsonify({'result': True})

# ** admin use only
# Endpoint for updating an app details
@uwp.route("/<string:id>", methods=['PUT'])
def update(id):
    app=db.find_one({"id":id})
    if app is None:
        return jsonify({'result': False})
    else:
        db.update({"id":id},{"$set":request.get_json()})
    return jsonify({'result': True})


p = Pool(10)
p.map(insert, all_urls)
p.terminate()
p.join()