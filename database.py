from bson.objectid import ObjectId
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "todo_db"
COLLECTION_NAME = "tasks"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
tasks_collection = db[COLLECTION_NAME]


def to_dict(task):
    task = dict(task)
    task["id"] = str(task["_id"])
    task.pop("_id", None)
    return task


def get_all_tasks():
    return [to_dict(task) for task in tasks_collection.find()]


def get_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        return to_dict(task)
    return None


def create_task(task_data):
    result = tasks_collection.insert_one(task_data)
    new_task = task_data.copy()
    new_task["id"] = str(result.inserted_id)
    return new_task


def update_task(task_id, update_data):
    result = tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})
    return result.modified_count > 0


def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count > 0
