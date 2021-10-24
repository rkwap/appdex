from apps import *
import play_scraper
play = APIRouter()

db = db.get_collection("play")
MAX_RESULTS=5


@play.get("/{q}")
def read_root(q):
  q = q.replace('+',' ')
  regx = re.compile(q, re.IGNORECASE)
  search = play_scraper.search(q)
  # apps = db.find({"$or":[{"title": regx}, {"developer": regx}, {"id":q}]}).limit(MAX_RESULTS)
  # data = {}
  # # if app already exists, then fetch details from DB
  # if apps is not None:
  #   data = []
  #   for app in apps:
  #     data.append(
  #       {
  #         "id":app["id"],
  #         "title":app["title"],
  #         "url":app["url"],
  #         "developer":app["developer"],
  #         "developer_url":app["developer_url"],
  #         "icon":app["icon"],
  #         "price":app["price"],
  #         "developer_email":app['developer_email']
  #       }
  #     )
  return {"data": search}

@play.post("/{q}")
def insert(q):
  q = q.replace(' ','+')
  search = play_scraper.search(q)
  for app in search:
    data = {
      "id": app['app_id'],
      "title": str(app['title']),
      "url": "https://play.google.com" + str(app['url']),
      "developer": str(app['developer']),
      "icon": str(app['icon']),
      "price": str(app['price']),
      "developer_url": "https://play.google.com/store/apps/developer?id=" + (app['developer'].replace(' ','+')),
      "developer_email": ""
    }
    # Saving/Updating the app details to DB
    db.update({ "id": app['app_id'] }, { "$set": data }, { "upsert": True })
  # q = q.replace(' ','+')
  return {"success": "true"}





# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
  # return {"item_id": item_id, "q": q}

