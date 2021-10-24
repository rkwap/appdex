import os,sys,inspect
c_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
p_dir = os.path.dirname(c_dir)
sys.path.insert(0,p_dir) 
from apps import app, uvicorn

if __name__ == "__main__":
    uvicorn.run("apps:app", port=7000, reload=True)

# uvicorn apps:app --port=7000 --reload
