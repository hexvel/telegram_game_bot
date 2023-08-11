import pymongo


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client.gameBot

    def insert_one(self, **data: object):
        try:
            insert = self.db.hexvel.insert_one(data)
            return {"is_done": True, "result": insert}
        except Exception as ex:
            return {"is_done": False, "error": ex}

    def insert_many(self, data: list):
        try:
            insert = self.db.hexvel.insert_many(data)
            return {"is_done": True, "result": insert}
        except Exception as ex:
            return {"is_done": False, "error": ex}

    def update_one(self, item, update):
        try:
            update = self.db.hexvel.update_one(item, update)
            return {"is_done": True, "result": update}
        except Exception as ex:
            return {"is_done": False, "error": ex}

    def find_one(self, data=None):
        try:
            find = self.db.hexvel.find_one(data)
            return {"is_done": True, "result": find}
        except Exception as ex:
            return {"is_done": False, "error": ex}

    def find(self, data=None):
        try:
            data_list = []
            find = self.db.hexvel.find(data)
            for doc in find:
                data_list.append(doc)

            return data_list
        except Exception as ex:
            return {"is_done": False, "error": ex}

    def find_and_replace(self, item: object, replace: object):
        try:
            find_and_replace = self.db.hexvel.find_one_and_replace(
                item, replace)
            if find_and_replace is not None:
                return {"is_done": True, "result": find_and_replace}
            else:
                return {"is_done": False, "result": f"{item} is not exist."}
        except Exception as ex:
            return {"is_done": False, "error": ex}

    def find_and_delete(self, data: object):
        try:
            find_and_delete = self.db.hexvel.find_one_and_delete(data)
            if find_and_delete is not None:
                return {"is_done": True, "result": find_and_delete}
            else:
                return {"is_done": False, "result": f"{data} is not exist."}
        except Exception as ex:
            return {"is_done": False, "error": ex}
