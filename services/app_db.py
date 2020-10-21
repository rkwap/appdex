import os,sys,inspect
c_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
p_dir = os.path.dirname(c_dir)
sys.path.insert(0,p_dir) 
from app_db import app

if __name__ == "__main__":
    app.secret_key = os.urandom(22)
    app.run(host = "0.0.0.0",debug=True, port=5000)
