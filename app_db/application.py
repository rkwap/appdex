# for all the common endpoints
from app_db import *

def search(db):
	cursor, total_count = GetAppQuery(db, { 'filters': get_filter_data(dict(request.args)) })
	data = AppSerializer(cursor)
	return build_response(data=data, total_count=total_count)

def delete(id, db):
	app = db.find_one({"id": id})
	if app is None:
		return build_response(success=False, error='App not found!', status_code=404)
	else:
		db.delete_one({"id": id})
	return build_response()

def update(id, db):
	app = db.find_one({"id": id})
	if app is None:
		return build_response(success=False, error='App not found!', status_code=404)
	else:
		db.update({"id": id}, {"$set": request.get_json()})
	return build_response()

def find_by_ids(ids, db):
	if ids is None:
		return build_response(success=False, error='Please enter atleast one or more ids')
	cursor = GetAppsFromIdsQuery(db, { 'ids': ids })
	data = AppListByIdsSerializer(cursor)
	return build_response(data=data)
	