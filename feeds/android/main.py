from feeds import *
android = Blueprint('android', __name__)

@android.route("/", methods=['GET'])
def search():
    data=query_db("SELECT * FROM public.users")
    print(data["username"])
    return (dict(data))
